---
name: multicanal-designer
description: Transforma os drafts de conteúdo (do multicanal-formatter) em ARTES PRONTAS PARA POSTAR (PNG) na identidade visual Horus Hub — carrossel/feed do Instagram, imagem do post de LinkedIn, thumbnail de YouTube e capa de TikTok/Reels. Use sempre que o usuário quiser "gerar a arte", "o design pronto pra postar", "transformar o roteiro em carrossel visual", "fazer as imagens do post/carrossel", ou criar peças visuais de marca para redes sociais. Usa templates HTML/CSS (Space Grotesk/Inter/Montserrat, dark #0a0a0f, gradiente roxo→azul, recurso [IA], handle @horushub.ia) renderizados com Chrome headless — texto perfeito, cores e fontes da marca exatas, 100% editável. É o terceiro estágio do pipeline de conteúdo Horus. Invoque mesmo sem a palavra "skill".
license: MIT
---

# Multicanal Designer

Pega o draft textual de uma peça (carrossel, post, roteiro) e gera a **arte final em PNG**, na marca **Horus Hub**, pronta para subir na plataforma. A legenda já vem do `multicanal-formatter`; aqui o foco é o **visual**.

A razão de existir: um roteiro de carrossel é texto; o que se posta é imagem. Gerar essa imagem à mão, slide a slide, é o gargalo entre "ideia pronta" e "publicado". Esta skill fecha o gargalo com templates de marca renderizados de forma reproduzível — e, por serem HTML, o texto sai perfeito e tudo é editável (ao contrário de imagem gerada por IA, que erra texto e foge da marca).

## Atalho: produção Horus usa o motor canônico

Para arte **Horus de produção** (feed 1080×1350, com o emblema oficial), prefira o **motor canônico**, que é a fonte de verdade do visual:

```
horus-core/docs/estrategia/05-criativos-conteudo-gtm/_criativos/horus_creative_engine.py
  → render_criativos(items, out_dir)   # items = lista de dicts (style, kicker, headline, sub, big, rows, cta, swipe)
```

Os `assets/` desta skill são o **tema público equivalente** (mesmas cores/fontes/layout, emblema em placeholder CSS) — para uso fora do ambiente Horus, outros canais (LinkedIn/YouTube/TikTok) ou quando o motor não estiver acessível.

## Como funciona (tema público)

`brand.css` (marca) + `assets/templates/*.html` (modelos) → o agente compõe os HTMLs finais → `scripts/render.py` rasteriza com Chrome headless → PNGs.

Pré-requisito: **Google Chrome instalado** (auto-detectado; senão passe `--chrome`). Sem libs nativas.

## Workflow

### Passo 1 — Ler as specs

Leia `references/design-specs.md`: o sistema (cores/fontes/glows/[IA]), os **4 estilos** (default/data/mantra/offer), as dimensões por canal e as zonas seguras.

### Passo 2 — Preparar a pasta de render

Crie a pasta da peça (ex.: `output/<slug>/instagram/arte-ideia-NN/`) e **copie `assets/brand.css` para dentro dela** (os templates referenciam `href="brand.css"` na mesma pasta).

### Passo 3 — Compor os HTMLs

Para cada arte/slide, copie o template do estilo adequado e preencha o conteúdo do draft (você está **diagramando, não reescrevendo** — a copy e a voz vêm do formatter):

- **Carrossel IG:** combine estilos — capa `feed-default`, slides de número `feed-data`, bordão `feed-mantra`, planos/portfólio `feed-offer`; último slide com CTA informativo.
- **LinkedIn:** `linkedin-square` (tese na imagem; texto na legenda).
- **YouTube:** `youtube-thumb` (≤5 palavras).
- **TikTok/Reels:** `tiktok-cover` (hook, respeitando a zona segura).

Regras: destaque (`.hl`/gradiente) só na palavra que carrega a tensão; `[IA]` só em palavra com "ia"; **dado sempre com fonte** (coerente com o guardrail de não inventar número); marca e `@horushub.ia` em toda peça.

### Passo 4 — Renderizar

```bash
# carrossel/pasta inteira (IG feed)
python scripts/render.py "<pasta>" --width 1080 --height 1350
# arte única — ajuste width/height pela tabela das specs (LinkedIn 1080x1080, YT 1280x720, TikTok 1080x1920)
python scripts/render.py "<arquivo>.html" --out "<saida>.png" --width 1280 --height 720
```

A dimensão precisa bater com a classe `canvas--*` do HTML.

### Passo 5 — Conferir e entregar

Abra os PNGs (legibilidade, contraste, marca correta). Entregue a pasta de artes + os HTMLs (editáveis) junto da legenda do formatter. São **artes prontas para revisão/publicação** — não publicadas automaticamente (isso é o `conteudo-scheduler`).

## Princípios

- **Diagramar, não reescrever.** Conteúdo e voz vêm do `multicanal-formatter` (guardrail OAB já aplicado).
- **Uma fonte de verdade visual.** Produção Horus → motor canônico; o tema público espelha-o. Não deixe os dois divergirem.
- **Editável por princípio.** Entregue os HTMLs junto dos PNGs: ajustar uma palavra e re-renderizar leva segundos.
- **Marca consistente, ritmo variado.** Mesma paleta/fontes; varie estilo e fundo para a série não cansar.
