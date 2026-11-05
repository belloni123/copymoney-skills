# Copymoney

`copymoney-copywriter` é uma habilidade em português para escrever e revisar landing pages, páginas de venda, campanhas, anúncios e conteúdo orgânico. Ela usa o briefing e a voz de cada marca e consulta um acervo com fichas de copywriting, referências e exemplos.

## Comece por aqui

| Onde você quer usar | Instalação | Como ativar |
|---|---|---|
| Codex no computador | [Instalar no Codex](#codex-no-computador) | Digite `$` no prompt e selecione `copymoney-copywriter`. |
| Claude Code | [Instalar no Claude Code](#claude-code) | Comece o prompt com `/copymoney-copywriter`. |
| ChatGPT | [Importar o ZIP](#chatgpt) | Digite `@` no chat e selecione `copymoney-copywriter`. |
| Codex Cloud | [Configurar o ambiente](#codex-cloud) | Selecione a habilidade ou indique o caminho do `SKILL.md`. |

## Codex no computador

1. Tenha o Codex e o Git instalados. No macOS ou Linux, abra o Terminal e rode:

   ```sh
   git clone https://github.com/belloni123/copymoney-skills.git
   cd copymoney-skills
   sh scripts/install-skill.sh codex
   ```

2. Abra uma nova sessão do Codex na pasta do projeto que você quer trabalhar. Pode ser uma pasta diferente da que você clonou.
3. No campo do prompt, digite `$`, procure **copymoney-copywriter** e selecione a habilidade. No Codex CLI, você também pode usar `/skills` para encontrá-la.
4. Depois da menção, escreva o pedido. Por exemplo:

   ```text
   $copymoney-copywriter Leia o briefing e revise a landing de inscrição. Preserve a oferta e o CTA.
   ```

Use o [primeiro teste](#primeiro-teste) se quiser conferir a instalação sem precisar de um briefing.

[Documentação do Codex sobre habilidades](https://learn.chatgpt.com/docs/build-skills)

## Claude Code

1. Tenha o Claude Code e o Git instalados. No macOS ou Linux, abra o Terminal e rode:

   ```sh
   git clone https://github.com/belloni123/copymoney-skills.git
   cd copymoney-skills
   sh scripts/install-skill.sh claude
   ```

   Se você já clonou o repositório para instalar no Codex, entre naquela pasta e rode apenas o instalador.

2. Abra uma nova sessão do Claude Code na pasta do projeto que você quer trabalhar.
3. No **prompt do Claude Code**, comece com `/copymoney-copywriter`, deixe um espaço e escreva o pedido. Por exemplo:

   ```text
   /copymoney-copywriter Leia o briefing e os exemplos de voz desta pasta. Revise a landing de inscrição, preserve a oferta e o CTA e liste à parte as alegações que ainda precisam de prova.
   ```

Para instalar nos dois agentes de uma vez, rode `sh scripts/install-skill.sh both` dentro do clone. O instalador usa a mesma pasta da habilidade para os dois.

[Documentação do Claude Code sobre habilidades](https://code.claude.com/docs/en/skills)

## ChatGPT

1. Baixe [copymoney-copywriter.zip](https://github.com/belloni123/copymoney-skills/releases/latest/download/copymoney-copywriter.zip).
2. No ChatGPT, abra **Plugins → Skills → Create → Upload from your computer** e selecione o ZIP inteiro.
3. Quando a habilidade estiver disponível, abra um novo chat. Digite `@`, selecione **copymoney-copywriter** e escreva o pedido.
4. Para usar materiais do seu cliente, anexe os arquivos pertinentes ou indique os que já estão disponíveis no projeto.

O menu Skills e a permissão de upload dependem do plano e das configurações do workspace. [Disponibilidade e upload de habilidades no ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## Codex Cloud

1. Crie ou selecione um ambiente Codex Cloud conectado ao repositório `belloni123/copymoney-skills`. Se ele não aparecer na lista, confira a conexão com o GitHub e o acesso ao repositório.
2. Abra uma nova tarefa nesse ambiente. Se a habilidade estiver no seletor, selecione **copymoney-copywriter**. Caso contrário, comece o prompt com: “Leia `.agents/skills/copymoney-copywriter/SKILL.md` e siga as referências indicadas para este pedido.”
3. Cole o pedido, por exemplo o teste abaixo. O acervo acompanha o checkout do ambiente.

[Documentação de ambientes do Codex Cloud](https://learn.chatgpt.com/docs/environments/cloud-environments)

## Primeiro teste

Ative a habilidade com o comando da sua ferramenta e mande este pedido:

> Descreva em até 70 palavras uma luminária com braço articulado e três níveis de intensidade, pensada para leitura à noite. Use apenas essas informações. Depois da descrição, cite uma ficha do acervo pelo ID e diga qual decisão do texto ela orientou.

Confira se a resposta usa os detalhes fornecidos, indica uma ficha e evita inventar preço, garantia ou especificações. Para um trabalho real, indique os arquivos do cliente e diga o que você quer receber. Por exemplo: “Leia o briefing, a landing atual e os exemplos aprovados de voz. Reescreva a abertura para quem chega pelo anúncio, mantenha o CTA e sinalize as promessas que precisam de prova.”

## Atualizar e resolver problemas

- **Codex e Claude Code:** rode `git pull --ff-only` dentro do clone usado na instalação. Abra uma nova sessão após atualizar.
- **ChatGPT:** baixe o ZIP da [release mais recente](https://github.com/belloni123/copymoney-skills/releases/latest) para atualizar a importação quando houver um pacote novo.
- **A habilidade não aparece:** reinicie o agente e confirme que a pasta clonada continua no mesmo lugar. Se estiver em um disco externo, confira se ele está montado. No ChatGPT, verifique se a importação já aparece na aba Skills do workspace ativo.
- **O instalador encontrou outra instalação:** verifique o destino com `ls -ld ~/.agents/skills/copymoney-copywriter` para Codex ou `ls -ld ~/.claude/skills/copymoney-copywriter` para Claude Code. Se o destino for um link simbólico antigo que você quer substituir, remova apenas esse link com `unlink` e rode o instalador novamente.
- **Remover a instalação local:** confirme com `ls -ld` que o destino é o link criado pelo instalador e use `unlink` no caminho correspondente. O clone e o acervo ficam no disco.

## Acervo e contribuições

- [Instruções da habilidade](.agents/skills/copymoney-copywriter/SKILL.md) e [modelo de briefing](.agents/skills/copymoney-copywriter/references/briefing.md)
- [Guia de landing pages](.agents/skills/copymoney-copywriter/references/guias/landing-pages.md)
- [Como consultar e manter o acervo](.agents/skills/copymoney-copywriter/references/acervo/README.md), [catálogo TSV](.agents/skills/copymoney-copywriter/references/acervo/catalogo.tsv) e [índice de fichas](.agents/skills/copymoney-copywriter/references/acervo/fichas.md)
- [Avaliação editorial e limites](AVALIACAO.md), [lacunas do acervo](.agents/skills/copymoney-copywriter/references/acervo/lacunas.md) e [procedência dos originais](.agents/skills/copymoney-copywriter/references/acervo/originais/README.md)

Para sugerir uma correção, abra uma [issue](https://github.com/belloni123/copymoney-skills/issues) com o ID da ficha ou o trecho do guia. Ao editar o acervo, rode `python3 scripts/verify-library.py` na raiz do clone para conferir os vínculos, as fontes e o formato. Use exemplos fictícios ou autorizados ao contribuir e mantenha briefings e dados de clientes no projeto privado correspondente.
