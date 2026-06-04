---
name: doc-idea-miner
description: Lê um documento longo e denso (PDF, Markdown, TXT — voto, provimento, paper técnico, ebook, transcrição) e extrai um BANCO DE IDEIAS estruturado para conteúdo. Use sempre que o usuário tiver um material extenso e quiser "tirar várias ideias de post/vídeo/conteúdo disso", "minerar ângulos", "transformar este documento em pauta", ou alimentar a produção de conteúdo a partir de uma fonte densa. É o primeiro estágio do pipeline de conteúdo Horus — a saída (banco de ideias) alimenta o multicanal-formatter. Invoque mesmo que o usuário não diga "skill": basta haver um documento longo + intenção de extrair ideias.
license: MIT
---

# Doc Idea Miner

Transforma um documento longo e denso numa **lista de ideias publicáveis**, cada uma já com o material bruto necessário para virar conteúdo: o ângulo, a tensão, o insight e — crucialmente — a **citação/dado âncora** tirada do próprio documento.

A razão de existir: ler um PDF de 80 páginas e "ter boas ideias" é trabalho que se perde se não for estruturado. Uma ideia solta ("falar sobre prescrição") não vira conteúdo; uma ideia ancorada ("o STJ fixou que o prazo só corre da ciência inequívoca — pág. 12 — isso contraria o que 90% dos contratos assumem") vira. Esta skill força a segunda forma.

## Quando usar

- O usuário tem um documento extenso (jurídico, técnico, acadêmico) e quer extrair pautas/ideias de conteúdo.
- O usuário quer "aproveitar" um material denso para redes sociais, newsletter, vídeos.
- Como **estágio 1** do `horus-conteudo-pipeline` (orquestrador). Pode rodar sozinha.

Não use para: resumir um doc curto (faça direto), gerar o post final (isso é o `multicanal-formatter`), ou pesquisar um tema sem documento-fonte (use `content-structure`).

## Workflow

### Passo 1 — Extrair o texto do documento

Não tente ler o PDF "no olho". Rode o script, que entrega texto limpo + um índice de seções:

```bash
python scripts/extract.py "<caminho-do-documento>"
```

Ele imprime um JSON com `out_path` (texto limpo), `words`, `headings[]` e `long_doc`. Leia o `out_path`.

- Se `long_doc` for `true` (>8000 palavras): **não** tente segurar tudo na cabeça de uma vez. Navegue por seção usando os `headings`, minere ideias seção a seção, e só então consolide. Densidade > cobertura: 12 ideias fortes valem mais que 40 rasas.
- Markdown/TXT também passam pelo script (normaliza e indexa). PDF exige `pypdf` (`py -m pip install pypdf`).

### Passo 2 — Minerar ideias (o coração)

Leia `references/extraction-heuristics.md` antes de começar. Ele lista os **gatilhos de ideia publicável** — onde, num texto denso, moram as ideias que viram conteúdo (afirmações contraintuitivas, números surpreendentes, frameworks, erros comuns, antes/depois, definições que mudam decisão). Caçar esses gatilhos é mais produtivo que "resumir".

Para cada ideia encontrada, extraia os campos do **banco de ideias**. O schema completo está em `references/banco-de-ideias-schema.md`. Em resumo, cada ideia tem:

- **núcleo** — a ideia central em uma frase memorável
- **ângulo** — a perspectiva específica que a torna interessante
- **tensão** — o conflito/problema/surpresa que prende atenção
- **insight** — a verdade não-óbvia que o leitor leva
- **âncora** — a citação, número ou trecho **literal do documento** que sustenta a ideia (com referência: "pág. 12" / seção)
- **público** — para quem essa ideia fala
- **canal_sugerido** — onde ela rende mais (instagram / linkedin / tiktok / youtube) e por quê

A âncora é obrigatória e é o que separa esta skill de "inventar conteúdo": toda ideia tem que ser rastreável ao documento. Se você não acha uma âncora, a ideia provavelmente não está no documento — descarte ou marque como `âncora: [não encontrada — hipótese do agente]`.

### Passo 3 — Montar o banco de ideias

Use `templates/banco-de-ideias-template.md` como estrutura de saída. Entregue:

1. Um **cabeçalho** com o documento-fonte, data e nº de ideias.
2. As ideias numeradas, cada uma com os campos acima.
3. Uma seção final **"Máquina de Ideias"**: 3–5 eixos temáticos que agrupam as ideias, para o usuário ver padrões e planejar uma série.

Salve em `banco-de-ideias.md` (ou no caminho que o orquestrador indicar). Se rodando dentro do `horus-conteudo-pipeline`, este arquivo é a interface que o `multicanal-formatter` consome.

## Princípios

- **Ancoragem acima de volume.** Uma ideia sem âncora no documento não é mineração, é invenção. Prefira menos ideias, todas rastreáveis.
- **Ângulos diversos sobre o mesmo núcleo.** Um bom documento rende vários ângulos para o mesmo fato — explore-os; é daí que sai uma série de conteúdo, não um post avulso.
- **Pensa em quem consome, não em quem escreveu.** O autor do documento otimizou para precisão; você minera para relevância. "Por que isso importa para um advogado/empresário/leigo?" é a pergunta que separa ideia boa de citação seca.
- **Não formate ainda.** Aqui você produz matéria-prima estruturada, não posts. A voz e o formato por canal são responsabilidade do `multicanal-formatter` — manter os estágios separados deixa cada um testável e reusável.
