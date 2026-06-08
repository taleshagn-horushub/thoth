---
name: conteudo-scheduler
description: Monta um calendário de publicação para as peças de conteúdo já produzidas e exporta em CSV, Markdown e um JSON pronto para o Postiz. Use sempre que o usuário quiser "agendar os posts", "montar o calendário de conteúdo", "distribuir as publicações na semana/mês", "definir quando postar cada peça", ou organizar a cadência de publicação nas redes. Distribui as peças por canal respeitando uma cadência (configurável) e não depende de integração externa — gera export importável em qualquer agendador. É o quarto estágio do pipeline de conteúdo Horus. Invoque mesmo sem a palavra "skill".
license: MIT
---

# Conteúdo Scheduler

Pega as peças prontas (legendas do `multicanal-formatter` + artes do `multicanal-designer`) e as organiza num **calendário de publicação**: que peça vai em qual canal, em que dia e hora. Exporta em três formatos para você publicar do jeito que preferir.

A razão de existir: ter 12 peças prontas não é ter um plano de publicação. Distribuí-las com ritmo (sem postar tudo no mesmo dia, sem furos de uma semana) é o que sustenta presença. E matemática de calendário — "próxima terça às 9h, sem colidir com a peça anterior" — é justamente onde o trabalho manual erra. O script resolve isso de forma determinística.

Escopo desta versão: gera o **plano e o export**. Não publica sozinho — a publicação automática (Postiz conectado / APIs Meta/LinkedIn) é o próximo estágio. O `postiz-ready.json` já sai no formato certo para quando essa integração existir.

## Workflow

### Passo 1 — Montar a lista de peças

Crie um `pieces.json` com as peças a agendar. Cada item: canal + título + (opcional) caminho da arte e da legenda.

```json
[
  {"channel": "linkedin",  "title": "Comece pela melhoria rápida", "asset": "linkedin/drafts.md", "caption": "linkedin/drafts.md"},
  {"channel": "instagram", "title": "A IA que dá lucro é invisível", "asset": "instagram/arte-ideia-02/", "caption": "instagram/drafts.md"},
  {"channel": "tiktok",    "title": "O risco da inatividade", "asset": "tiktok/drafts.md"}
]
```

`channel` ∈ `instagram` | `linkedin` | `tiktok` | `youtube`.

### Passo 2 — (Opcional) Ajustar a cadência

A cadência default (padrão Horus: Instagram é o feed diário; demais apoiam) é:

| Canal | Dias | Hora |
|-------|------|------|
| Instagram | seg–sáb (1 post/dia útil) | 18:00 |
| LinkedIn | ter, qui | 09:00 |
| TikTok/Reels | seg, qua, sex | 12:00 |
| YouTube | qua (semanal) | 19:00 |

O calendário também sugere o **pilar de conteúdo** por dia (rodízio Educar/Demonstrar/Processo/Autoridade/Oferta), espelhando a estratégia Horus (`horus-core/docs/estrategia/05-criativos-conteudo-gtm/calendario-30-dias.md`). É guia editorial — não muda a alocação de datas.

Para mudar, crie um `cadence.json` (sobrescreve só os canais que você listar). `weekday`: 0=segunda … 6=domingo.

```json
{ "linkedin": {"weekdays": [1, 4], "time": "08:30"} }
```

### Passo 3 — Gerar o calendário

```bash
python scripts/build_calendar.py pieces.json --start 2026-06-09 --out "<pasta-de-saída>"
# com cadência custom:
python scripts/build_calendar.py pieces.json --start 2026-06-09 --cadence cadence.json --out "<pasta-de-saída>"
```

`--start` é a data (AAAA-MM-DD) a partir da qual distribuir. Passe a data real de início do plano — o script não adivinha "hoje", para o resultado ser determinístico.

### Passo 4 — Entregar

O script gera três arquivos na pasta de saída:

- **`calendar.csv`** — data, hora, dia, canal, título, arte, legenda, status. Importável em Google Sheets, Notion, ou qualquer agendador.
- **`calendar.md`** — calendário legível, agrupado por semana, para revisão rápida.
- **`postiz-ready.json`** — payload estruturado (`publishAt` ISO + canal + caminhos) pronto para a integração de publicação futura (Postiz/API).

Apresente o `calendar.md` ao usuário para revisão e aponte o CSV/JSON para uso operacional. Deixe claro que o plano é **proposto** — datas e horários são ajustáveis (regenere mudando `--start` ou a cadência).

## Princípios

- **Determinístico.** Mesmas peças + mesmo `--start` + mesma cadência → mesmo calendário. É o que torna o plano confiável e regenerável.
- **Ritmo, não rajada.** A cadência distribui as peças para sustentar presença, em vez de despejar tudo num dia.
- **Neutro de ferramenta.** Exporta em formatos abertos (CSV/MD/JSON) — não amarra você a um agendador específico. O `postiz-ready.json` é a ponte para automação quando ela chegar.
- **Plano, não publicação.** Esta skill organiza; publicar é decisão e estágio à parte.
