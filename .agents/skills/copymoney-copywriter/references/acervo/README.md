# Como consultar o acervo

O [catálogo](catalogo.tsv) é o inventário curado. O [índice de fichas](fichas.md) permite procurar por autor e problema, e as fichas têm o localizador no material. O [índice de Halbert](indice-halbert.tsv) registra os destinos individuais identificáveis nas duas páginas oficiais de arquivo. A [lista de lacunas](lacunas.md) registra cobertura e próximas fontes.

## O que o acervo contém de fato

No corte de 5 de novembro de 2026, são 44 referências curadas: **22 apenas catalogadas, 10 consultadas parcialmente e 12 consultadas como unidade**. As 34 fichas se apoiam em **19 IDs de fonte distintos**; seis fichas de Hopkins vêm de capítulos de um único livro. Há um PDF integral de Hopkins guardado localmente, mas a leitura registrada cobre capítulos selecionados. *Ogilvy on Advertising* também foi consultado em parte. O registro `cap-tested-1975` é uma citação de Caples reproduzida por Ogilvy, não uma leitura do livro de Caples.

Os 220 destinos no índice de Halbert são um inventário de links, não 220 textos lidos. Os livros de Schwartz, Kennedy, Brunson, Hormozi e Cialdini listados no catálogo ainda não sustentam fichas por leitura integral. As fichas desses nomes vêm dos trechos, cartas, artigos ou páginas institucionais especificados em cada uma. A cobertura de dez autores significa **dez autores representados**, não domínio de seus métodos completos. Para escolher um princípio, confira sempre o alcance da leitura, o localizador e a distância entre a fonte e a aplicação Copymoney.

1. Busque o problema ou formato em `fichas.md` com `rg -in 'benefício|prova|landing' fichas.md`, ou leia o índice diretamente.
2. Abra a ficha de interesse e busque seu ID de fonte em `catalogo.tsv`, por exemplo `rg '^mak-sparkle\b' catalogo.tsv`.
3. Em respostas sobre o acervo, indique o ID da ficha, o ID da fonte, o localizador e o link. Se uma obra estiver só catalogada, apresente o caminho de acesso. Ao usar duas fichas para comparar autores, atribua a cada um somente o que seu material sustenta.
4. Para pesquisar o arquivo de Halbert, procure também no inventário complementar. Um item indexado confirma que o título e o link aparecem no arquivo, sem confirmar a autoria, a disponibilidade ou o conteúdo de cada destino.

## Como manter

O TSV usa UTF-8, cabeçalho e um registro por linha. IDs têm prefixo de autor e não mudam quando o link muda. Use `—` para dado desconhecido e `relacionado` para ligar outra edição, tradução ou material pertencente a uma coleção. Verifique pelo autor, editor ou biblioteca e diferencie edições quando alterarem texto, capítulos ou crédito de autoria.

- `catalogado`: título e acesso identificados por referência bibliográfica, sumário, índice ou oferta do editor.
- `parcial`: texto, anúncio, trecho ou seção de fato examinados, com escopo na nota.
- `consultado`: material identificado na linha examinado como unidade, mesmo quando é parte de uma obra maior.
- `citação secundária`: o trecho de um autor foi encontrado em outra obra. O registro deve nomear quem o reproduziu e não pode ser apresentado como leitura da obra original.
- No índice de Halbert, os IDs derivam do URL do destino. As páginas oficiais misturam textos do autor, contribuições de terceiros, reedições e links restritos. Um item passa ao catálogo curado após confirmar a atribuição e registrar o acesso. Preserve o vínculo com o item do índice.

Para acrescentar uma ficha, use a estrutura das existentes e inclua o link no índice. Uma alegação de desempenho feita na própria publicidade é material para estudar a peça, sem servir como validação independente. Prefira paráfrase e exemplos próprios. Guarde originais apenas com direito de redistribuir a edição específica, citando procedência em `originais/README.md`. Materiais particulares e briefings podem ficar em `materiais-privados/` ou `briefings-privados/` na raiz do projeto.
