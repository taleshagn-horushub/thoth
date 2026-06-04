---
name: horus-conteudo-pipeline
description: Pipeline de ponta a ponta que transforma um documento longo e denso (PDF, MD, TXT) em conteúdo pronto para postar nos 4 canais do Horus — Instagram, LinkedIn, TikTok, YouTube — incluindo arte visual e calendário de publicação. Use sempre que o usuário entregar um documento e pedir "transforma isso em conteúdo", "gera posts/vídeos a partir deste material", "quero pautas, arte e calendário desse PDF para as redes", ou quiser rodar o fluxo de conteúdo completo de uma vez. Orquestra quatro skills (doc-idea-miner → multicanal-formatter → multicanal-designer → conteudo-scheduler) com guardrail de voz Horus e compliance OAB, e grava tudo em output/<slug>/. É o ponto de entrada único do Fluxo de Conteúdo (#05). Invoque mesmo sem a palavra "skill".
license: MIT
---

# Horus Conteúdo Pipeline

Encadeia o fluxo completo **documento → ideias → conteúdo nativo → arte → calendário**, em um comando conceitual. É a porta de entrada do Fluxo de Conteúdo do Horus: o usuário dá um documento, a skill devolve uma pasta organizada com o banco de ideias, os drafts dos 4 canais (voz Horus + OAB), as artes PNG prontas para postar e um calendário de publicação.

A razão de ser um orquestrador separado: os estágios (`doc-idea-miner`, `multicanal-formatter`, `multicanal-designer`, `conteudo-scheduler`) são úteis isolados, mas na prática o usuário quase sempre quer o caminho inteiro. Esta skill cola os estágios, define a estrutura de saída e garante que o guardrail rode. Mantê-la fina (só orquestração) deixa os estágios livres para evoluir sozinhos.

## Entradas

- **Documento** (obrigatório): caminho de um `.pdf`, `.md` ou `.txt`.
- **Canais** (opcional): subconjunto de `{instagram, linkedin, tiktok, youtube}`. Default: todos os quatro, mas confirme com o usuário.
- **Quantas ideias formatar** (opcional): por padrão, formate as 3–5 ideias mais fortes do banco em conteúdo; as demais ficam no banco para uso futuro. Confirme se o usuário quer todas.

## Workflow

### Estágio 0 — Preparar saída

Defina um `slug` a partir do nome do documento (kebab-case, sem acento). Crie a pasta de saída `output/<slug>/`. Todos os artefatos vão para lá.

### Estágio 1 — Minerar (doc-idea-miner)

Invoque a skill `doc-idea-miner`:
1. Rode o `extract.py` dela para obter texto limpo + estrutura.
2. Produza o **banco de ideias** seguindo as heurísticas e o schema dela.
3. Salve em `output/<slug>/banco-de-ideias.md`.

Se o documento for longo (`long_doc: true`), respeite a instrução do miner de minerar por seção antes de consolidar.

### Estágio 2 — Priorizar

Do banco, selecione as ideias a formatar agora (default: 3–5 mais fortes — as com âncora mais sólida e maior relevância para o público). Para cada ideia, parta do `canal_sugerido`, mas gere para todos os canais pedidos pelo usuário. Mostre ao usuário a lista priorizada antes de formatar, para ele poder ajustar.

### Estágio 3 — Formatar + guardrail (multicanal-formatter)

Para cada ideia selecionada, invoque a skill `multicanal-formatter`:
- Gere o artefato nativo de cada canal pedido (lendo as referências de canal da skill).
- Rode o guardrail `voz-horus-oab.md` em **cada peça** (voz Horus + compliance OAB). Reescreva o que violar a OAB, sinalizando.

### Estágio 4 — Desenhar a arte (multicanal-designer)

Para cada peça formatada, invoque a skill `multicanal-designer`:
- Gere as artes PNG na marca Horus (carrossel IG, imagem LinkedIn, thumbnail YouTube, capa TikTok) via templates HTML + `render.py`.
- Copie o `brand.css` para cada pasta de render e confira legibilidade.

### Estágio 5 — Montar o calendário (conteudo-scheduler)

Monte o `pieces.json` (uma entrada por peça, com canal + título + caminho da arte e da legenda) e invoque a skill `conteudo-scheduler`:
- Rode o `build_calendar.py` com a data de início que o usuário indicar.
- Gera `calendar.csv`, `calendar.md` e `postiz-ready.json`.

### Estágio 6 — Gravar e relatar

Organize a saída assim:

```
output/<slug>/
├── banco-de-ideias.md
├── instagram/
│   ├── drafts.md                  ← legendas/roteiros (com guardrail OAB)
│   └── arte-ideia-02/             ← slides HTML + PNGs prontos + brand.css
├── linkedin/   (drafts.md + arte-*/)
├── tiktok/     (drafts.md + capa PNG)
├── youtube/    (drafts.md + thumbnail PNG)
└── calendario/
    ├── calendar.md
    ├── calendar.csv
    └── postiz-ready.json
```

Cada arquivo de draft começa com um cabeçalho rastreável: ideia-fonte (núcleo) + âncora do documento (pág./seção). Entregue ao usuário um resumo: quantas ideias no banco, quantas formatadas/desenhadas, quais canais, reescritas por compliance OAB, e o calendário proposto. Deixe explícito que são **peças prontas para revisão**, não publicadas automaticamente.

## Princípios

- **Um caminho, estágios separados.** A skill orquestra, mas não reimplementa: a inteligência de mineração mora no `doc-idea-miner` e a de formato no `multicanal-formatter`. Se algo precisa mudar em como se minera ou se formata, mexe-se no estágio, não aqui.
- **Rastreabilidade ponta a ponta.** A âncora do documento viaja da mineração até o draft final. Qualquer afirmação no conteúdo deve ser rastreável ao documento-fonte.
- **Guardrail sempre.** Nenhuma peça sai sem passar pela checagem de voz + OAB.
- **Drafts, não auto-publish.** A saída é para revisão humana. Publicação/agendamento (ex.: integração com agendador) está fora do escopo desta versão.

## Fora de escopo (versão atual)

**Publicação automática** nas redes (Postiz conectado / APIs Meta/LinkedIn), analytics de desempenho, e loop de feedback (desempenho → ajuste de pauta). A saída para em peças prontas + calendário proposto; o `postiz-ready.json` já é a ponte para a automação futura, consumindo a mesma pasta `output/<slug>/`.
