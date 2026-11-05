# Copymoney

Acervo de copywriting e skill para transformar briefings de marca em conteúdo orgânico, campanhas, páginas e criativos.

- [Habilidade](.agents/skills/copymoney-copywriter/SKILL.md)
- [Briefing](.agents/skills/copymoney-copywriter/references/briefing.md)
- [Como consultar e manter o acervo](.agents/skills/copymoney-copywriter/references/acervo/README.md)
- [Catálogo TSV](.agents/skills/copymoney-copywriter/references/acervo/catalogo.tsv)
- [Índice de fichas](.agents/skills/copymoney-copywriter/references/acervo/fichas.md)
- [Inventário de lacunas](.agents/skills/copymoney-copywriter/references/acervo/lacunas.md)
- [Guia de landing pages](.agents/skills/copymoney-copywriter/references/guias/landing-pages.md)
- [Avaliação editorial e limites](AVALIACAO.md)

## Instalação no Codex e no Claude Code

Clone o repositório público no Mac ou no Linux. Para disponibilizar a habilidade nos dois agentes, inclusive ao abrir o projeto de outro cliente, rode:

```sh
git clone https://github.com/belloni123/copymoney-skills.git
cd copymoney-skills
sh scripts/install-skill.sh both
```

Use `sh scripts/install-skill.sh codex` ou `sh scripts/install-skill.sh claude` para instalar em um só agente. O instalador vincula a mesma pasta de skill a `~/.agents/skills/copymoney-copywriter` no Codex e a `~/.claude/skills/copymoney-copywriter` no Claude Code. Preserve o clone no mesmo local e faça `git pull --ff-only` nele para atualizar. Se a pasta estiver em um disco externo, mantenha o volume montado durante o uso. O instalador informa se o destino já aponta para outro clone ou contém uma instalação independente.

## Como usar no prompt

Abra uma nova sessão no projeto do cliente e selecione a habilidade no início do prompt.

| Agente | Como chamar |
|---|---|
| Codex | Digite `$` e selecione `copymoney-copywriter`. No CLI, também pode usar `/skills`. |
| Claude Code | Comece com `/copymoney-copywriter` e escreva o pedido depois do comando. |
| ChatGPT com Skills | Digite `@` e selecione `copymoney-copywriter` após importar o ZIP. |

Exemplo para o Codex, usando a menção selecionada:

> Use $copymoney-copywriter. Leia o briefing e os exemplos de voz nesta pasta. Revise a landing de inscrição, preserve a oferta e o CTA e mostre o que você alterou. Separe as alegações que ainda dependem de prova.

No Claude Code, escreva `/copymoney-copywriter Leia o briefing e os exemplos de voz nesta pasta. Revise a landing de inscrição, preserve a oferta e o CTA e mostre o que você alterou.`

[Skills no Codex e no ChatGPT](https://learn.chatgpt.com/docs/build-skills) · [Skills no Claude Code](https://code.claude.com/docs/en/skills)

## Importação no ChatGPT

Baixe o [ZIP da habilidade](https://github.com/belloni123/copymoney-skills/releases/latest/download/copymoney-copywriter.zip). Em um workspace que ofereça Skills e permita upload, abra **Plugins → Skills → Create → Upload from your computer** e envie o ZIP. Depois, selecione a habilidade com `@` em um novo chat. Use o ZIP da release para atualizar a importação quando houver uma versão nova. [Disponibilidade e upload de Skills no ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex Cloud

Crie um ambiente Codex Cloud com o repositório Copymoney no GitHub. Se o repositório não aparecer, confira a conexão do GitHub e a permissão para esse repositório. O acervo pode ser lido diretamente no checkout. [Ambientes no Codex Cloud](https://learn.chatgpt.com/docs/environments/cloud-environments)

Em uma nova tarefa Cloud, peça para ler a habilidade e consultar as fichas. Se o seletor não listar a habilidade nessa superfície, indique explicitamente `.agents/skills/copymoney-copywriter/SKILL.md`. Para conferir a revisão, rode `git rev-parse HEAD` na tarefa e compare com a revisão instalada nos Macs.

Exemplo de teste:

> Use .agents/skills/copymoney-copywriter/SKILL.md. Localize no acervo uma ficha sobre benefício e outra sobre prova. Use-as para descrever em até 70 palavras uma luminária com braço articulado e três níveis de intensidade, para leitura à noite. Mostre a copy e, separadamente, os IDs e links das fontes. Use somente os arquivos deste checkout.

## Verificação

Na raiz, rode `python3 scripts/verify-library.py`. A verificação lê o catálogo e as fichas localmente e confere vínculos, procedência, cobertura e formato. Para ampliar o acervo, siga os critérios no guia de consulta.

Para usar a habilidade com um cliente novo, deixe seus materiais no projeto desse cliente ou em uma pasta privada indicada no pedido. Forneça oferta, condições, exemplos aprovados da voz da marca e, quando disponíveis, dúvidas e falas reais de compradores. A habilidade seleciona o argumento e a linguagem para esse contexto. Sem esses materiais, a primeira copy precisa de calibração editorial antes de publicação.
