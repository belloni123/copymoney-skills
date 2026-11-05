# Copymoney

O Copymoney é uma habilidade de copywriting em português para escrever do zero ou revisar o que já existe. Dê ao agente o briefing, a oferta e exemplos da voz da marca. Ele usa esses materiais e consulta o acervo para escolher o argumento, organizar a peça e escrever o texto. O acervo reúne **34 fichas práticas e 44 referências catalogadas**, com **dez autores representados**.

[O que você pode pedir](#o-que-você-pode-pedir) · [Autores do acervo](#quem-está-no-acervo) · [Instalar e ativar](#comece-por-aqui)

## O que você pode pedir

| Trabalho | O que a habilidade entrega |
|---|---|
| **Landing pages** | Escreve ou revisa a abertura, os blocos e o CTA. Usa a mensagem do anúncio ou da busca para decidir o que a página precisa esclarecer primeiro. |
| **Páginas de venda e descrições de produto** | Transforma características em usos concretos, organiza benefícios e objeções e explicita as condições relevantes da oferta. |
| **Anúncios e criativos** | Propõe ângulos, ganchos e variações. Para peças estáticas ou em vídeo, pode sugerir direção visual ou roteiro. |
| **Campanhas** | Conecta anúncio, página e sequência em torno da mesma promessa. Quando solicitado, propõe o que testar e como comparar as versões. |
| **Conteúdo orgânico** | Escreve posts, carrosséis, roteiros ou lotes editoriais com base no tema e na voz da marca. |

Você pode pedir a copy pronta ou uma revisão que explique as mudanças. A habilidade usa os materiais da marca para calibrar a voz, separa as alegações que precisam de prova e, quando solicitado, indica as fichas que orientaram suas decisões.

## Quem está no acervo

| Autor | Temas das fichas no Copymoney |
|---|---|
| **Claude Hopkins** | Títulos que selecionam o leitor, detalhes verificáveis e testes em pequena escala. |
| **John Caples** | Ganchos narrativos, benefícios mostrados em cena e comparação de apelos. |
| **David Ogilvy** | Pesquisa antes da escrita, posicionamento e provas concretas na abertura. |
| **Eugene Schwartz** | Desejo que o público já tem e ligação entre intenção, mensagem e oferta. |
| **Robert Cialdini** | Reciprocidade, prova social de pessoas comparáveis e escassez verificável. |
| **Gary Halbert** | Sinais de demanda, primeiros testes e pedidos de feedback. |
| **Clayton Makepeace** | Como traduzir características em benefícios observáveis e priorizar os mais relevantes. |
| **Dan Kennedy** | Redução de risco com condições claras e instruções para o próximo passo. |
| **Russell Brunson** | Sequência do funil, ganchos que conduzem à oferta e compromissos proporcionais a cada etapa. |
| **Alex Hormozi** | Mapeamento dos obstáculos do público e estruturação de uma oferta que facilite o uso. |

Cada ficha indica sua fonte e traz uma aplicação prática. O catálogo registra o que foi apenas identificado, o que foi consultado em parte e o que foi consultado por inteiro. [Índice de fichas](.agents/skills/copymoney-copywriter/references/acervo/fichas.md) · [Escopo do acervo](.agents/skills/copymoney-copywriter/references/acervo/README.md)

## Um exemplo na prática

No exemplo fictício do guia, uma oficina recebe câmeras mecânicas de 35 mm para diagnóstico. O anúncio já levanta a dúvida sobre a câmera funcionar de verdade.

| Rascunho | Abertura revisada |
|---|---|
| “Transforme sua experiência com fotografia analógica.” | “Ela dispara. Mas o filme avança?” |

A segunda abertura retoma a dúvida que trouxe o visitante até a página. O restante do texto informa o que a oficina verifica, o preço do diagnóstico, o prazo de entrega do relatório e como solicitá-lo. [Veja o briefing e a revisão completa](.agents/skills/copymoney-copywriter/references/guias/landing-pages.md#exemplo-original-inteiramente-fictício)

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
