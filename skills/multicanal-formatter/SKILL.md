---
name: multicanal-formatter
description: Transforma uma ideia (ou um banco de ideias do doc-idea-miner) em conteúdo NATIVO e pronto para revisão em até 4 canais — Instagram (carrossel + legenda), LinkedIn (post longo), TikTok (roteiro shot-a-shot), YouTube (roteiro + título + capítulos + thumbnail). Use sempre que o usuário quiser "virar esta ideia em post/carrossel/roteiro", "adaptar para Instagram e LinkedIn", "fazer conteúdo para os canais", ou formatar pautas para redes sociais. Aplica a voz da marca Horus e um guardrail de compliance OAB (Provimento 205/2021) em toda saída jurídica. É o segundo estágio do pipeline de conteúdo Horus; consome o banco de ideias e entrega drafts. Invoque mesmo sem a palavra "skill".
license: MIT
---

# Multicanal Formatter

Pega uma ideia já minerada e a entrega no **formato nativo de cada canal** — não uma legenda genérica replicada em quatro lugares, mas o artefato que cada plataforma realmente premia: um carrossel para o Instagram, um post de autoridade para o LinkedIn, um roteiro shot-a-shot para o TikTok, um roteiro com capítulos para o YouTube.

A razão de existir: o erro mais comum em conteúdo multicanal é escrever uma vez e colar em todo lugar. Cada plataforma tem gramática própria (ritmo, tamanho, gancho, formato visual). Esta skill encapsula essa gramática por canal, para que a mesma ideia renda quatro peças que parecem feitas para cada casa.

## Entrada e saída

**Entrada:** uma ideia no formato do banco (núcleo, ângulo, tensão, insight, âncora, público) — colada pelo usuário, ou lida de um `banco-de-ideias.md` produzido pelo `doc-idea-miner`. A skill roda isolada: se o usuário só descreve a ideia em texto livre, estruture-a mentalmente nos campos antes de formatar.

**Saída:** drafts em Markdown, **prontos para revisão humana** (não auto-publicados). Um arquivo por canal, ou uma pasta `output/<slug>/` com subpastas por canal quando vier do orquestrador.

## Workflow

### Passo 1 — Selecionar canais e ideias

Pergunte (ou receba do orquestrador): quais canais? quais ideias do banco? Se o usuário não especificar, use o `canal_sugerido` de cada ideia como default e confirme.

### Passo 2 — Aplicar a gramática de cada canal

Para **cada canal escolhido**, leia a referência correspondente e siga a estrutura, limites e checklist de lá:

- Instagram → `references/instagram.md`
- LinkedIn → `references/linkedin.md`
- TikTok → `references/tiktok.md`
- YouTube → `references/youtube.md`

Cada referência traz: a estrutura nativa, os limites (caracteres/duração), o que faz o conteúdo performar naquela plataforma, um checklist, e um **slot de "exemplo campeão"** — a peça real de melhor desempenho do usuário naquele canal. Quando o exemplo campeão estiver preenchido, **imite a estrutura e a voz dele**: exemplo concreto vence regra abstrata. Quando estiver vazio, siga a estrutura-base da referência e sinalize ao usuário que adicionar um exemplo campeão elevará a qualidade.

Reuso (não reinventar):
- Para **ganchos/legendas curtas** por tipo (autoridade, viral, storytelling…), a skill `social-media-captions` do thoth tem um mapa por plataforma — use como banco de hooks.
- Para o **roteiro longo de YouTube** com narrativa de venda, a skill `vsl-kishotenketsu-creator` cobre a estrutura Kishōtenketsu; reaproveite-a quando o vídeo for de oferta/posicionamento.

### Passo 3 — Passar pelo guardrail de voz + OAB (obrigatório)

Antes de entregar qualquer peça, leia `references/voz-horus-oab.md` e rode a checagem. Este passo **não é opcional para conteúdo jurídico**: o que sai daqui deve ser publicável sem revisão jurídica pesada.

O guardrail faz duas coisas:
1. **Voz Horus** — aplica o tom Sábio + Mago (autoridade com clareza, transformação sem sensacionalismo).
2. **Compliance OAB (Prov. 205/2021)** — bloqueia/reescreve promessa de resultado, captação ativa, preço de honorário, caso concreto identificável, sensacionalismo. Conteúdo jurídico tem caráter informativo/educativo, nunca mercantil.

Se uma ideia, do jeito que veio, não tem como ser dita sem violar a OAB, **reescreva o ângulo** para a forma informativa equivalente em vez de descartar — e sinalize a mudança ao usuário.

### Passo 4 — Entregar para revisão

Monte a saída com um cabeçalho identificando a ideia-fonte (e a âncora do documento, para rastreabilidade) seguido das peças por canal. Deixe claro que são drafts para revisão. Se algum campo dependeu de suposição (ex.: dado não confirmado), marque explicitamente.

## Princípios

- **Nativo, não replicado.** A mesma ideia deve soar feita para cada plataforma. Se o post do LinkedIn e a legenda do Instagram são idênticos, algo está errado.
- **A âncora viaja com a ideia.** Mantenha a rastreabilidade ao documento-fonte; é o que dá autoridade e protege contra "inventar" dado. Nunca crie estatística que não estava na ideia.
- **Guardrail é estágio, não enfeite.** A checagem OAB acontece em toda peça, sempre — não é um aviso no rodapé.
- **Draft honesto.** Entregue pronto para revisão, com suposições marcadas. Não finja certeza sobre dado que veio como hipótese.
