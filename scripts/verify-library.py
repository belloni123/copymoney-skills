#!/usr/bin/env python3
"""Check local catalog and skill invariants without network access."""

import csv
import re
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/copymoney-copywriter"
LIBRARY = SKILL / "references/acervo"
AUTHORS = {
    "Claude Hopkins", "John Caples", "David Ogilvy", "Eugene Schwartz",
    "Robert Cialdini", "Gary Halbert", "Clayton Makepeace", "Dan Kennedy",
    "Russell Brunson", "Alex Hormozi",
}


def require(condition, detail):
    if not condition:
        raise SystemExit(detail)


def load_index(name):
    with (LIBRARY / name).open(encoding="utf-8", newline="") as file:
        entries = {}
        for row in csv.DictReader(file, delimiter="\t"):
            require(None not in row and all(row.values()), f"{name}: linha incompleta")
            key = row["id"]
            require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", key), f"ID inválido: {key}")
            require(key not in entries, f"ID repetido: {key}")
            url = urlsplit(row["url"])
            require(url.scheme == "https" and url.hostname, f"URL inválido: {key}")
            entries[key] = row
    return entries


def main():
    catalog = load_index("catalogo.tsv")
    archive = load_index("indice-halbert.tsv")
    require(len(catalog) >= 30, "Catálogo tem menos de 30 materiais")
    require({row["autor"] for row in catalog.values()} == AUTHORS, "Cobertura de autores incompleta")
    require(not (catalog.keys() & archive.keys()), "ID compartilhado pelo catálogo e pelo arquivo")
    for key, row in catalog.items():
        parent = row["relacionado"]
        require(parent == "—" or (parent != key and parent in catalog), f"Vínculo inválido: {key}")
        require(row["status_leitura"] in {"catalogado", "parcial", "consultado"}, f"Status inválido: {key}")
        if row["acesso"] == "original_local":
            matches = re.findall(r"originais/[^\s;]+", row["nota"])
            require(len(matches) == 1 and (LIBRARY / matches[0]).is_file(), f"Original ausente: {key}")
    archive_urls = {row["url"] for row in archive.values()}
    require(len(archive_urls) == len(archive), "URL repetido no índice Halbert")
    for row in archive.values():
        key = row["catalogo_id"]
        require(key == "—" or (key in catalog and catalog[key]["url"] == row["url"]),
                f"Vínculo inválido no arquivo Halbert: {row['id']}")

    index = (LIBRARY / "fichas.md").read_text(encoding="utf-8")
    expected_cards = re.findall(r"\]\(fichas/([a-z0-9-]+)\.md\)", index)
    cards = sorted(card for card in (LIBRARY / "fichas").glob("[a-z]*.md")
                   if not card.name.startswith("."))
    require(sorted(expected_cards) == [card.stem for card in cards], "Índice de fichas divergente")
    require(len(cards) >= 30, "Menos de 30 fichas")
    authors = set()
    for card in cards:
        body = card.read_text(encoding="utf-8")
        source = re.search(r"^\*\*Fonte\.\*\* \[([^\]]+)\]\(([^)]+)\) · (.+)$", body, re.M)
        require(source and source[1] in catalog, f"Fonte desconhecida: {card.name}")
        row = catalog[source[1]]
        require(row["url"] == source[2], f"URL de ficha divergente: {card.name}")
        require(row["status_leitura"] != "catalogado", f"Fonte sem leitura: {card.name}")
        for field in ("Princípio na fonte", "Aplicação Copymoney", "Limite da aplicação", "Exemplo original"):
            require(re.search(rf"^\*\*{field}\.\*\* \S", body, re.M), f"Campo {field} ausente: {card.name}")
        authors.add(row["autor"])
    require(authors == AUTHORS, "Faltam autores nas fichas")

    for doc in (SKILL / "SKILL.md", *sorted((SKILL / "references/guias").glob("[a-z]*.md"))):
        for key in re.findall(r"`([a-z]{3}-\d{2})`", doc.read_text(encoding="utf-8")):
            require(key in expected_cards, f"Ficha citada não existe: {key}")

    print(f"OK · {len(catalog)} fontes curadas, {len(cards)} fichas, {len(authors)} autores "
          f"e {len(archive)} destinos no índice Halbert.")


if __name__ == "__main__":
    main()
