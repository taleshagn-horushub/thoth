---
name: multicanal-designer
description: Transforma os drafts de conteúdo (do multicanal-formatter) em ARTES PRONTAS PARA POSTAR (PNG) na identidade visual Horus — carrossel do Instagram, imagem do post de LinkedIn, thumbnail de YouTube e capa de TikTok/Reels. Use sempre que o usuário quiser "gerar a arte", "o design pronto pra postar", "transformar o roteiro em carrossel visual", "fazer as imagens do post/carrossel", ou criar peças visuais de marca para redes sociais. Usa templates HTML/CSS renderizados com Chrome headless (texto perfeito, cores e fontes da marca exatas, 100% editável). É o terceiro estágio do pipeline de conteúdo Horus. Invoque mesmo sem a palavra "skill".
license: MIT
---

# Multicanal Designer

Pega o draft textual de uma peça (carrossel, post, roteiro) e gera a **arte final em PNG**, na marca Horus, pronta para subir na plataforma. A legenda já vem do `multicanal-formatter`; aqui o foco é o **visual**.

A razão de existir: um roteiro de carrossel é texto; o que se posta é imagem. Gerar essa imagem à mão no Canva, slide a slide, é o gargalo entre "ideia pronta" e "publicado". Esta skill fecha esse gargalo com templates de marca renderizados de forma reproduzível — e, por serem HTML, o texto sai perfeito e tudo é editável (ao contrário de imagem gerada por IA, que erra texto e foge da marca).

## Como funciona (visão geral)

`brand.css` (marca) + `assets/templates/*.html` (modelos por canal) → o agente compõe os HTMLs finais da peça → `scripts/render.py` rasteriza com Chrome headless → PNGs prontos.

Pré-requisitos: **Google Chrome instalado** (o `render.py` auto-detecta; em outro caminho, passe `--chrome`). Sem libs nativas.

## Workflow

### Passo 1 — Ler as specs do canal

Leia `references/design-specs.md`. Ele traz, por canal: a **dimensão exata**, qual classe `canvas--*` usar, quais templates, as **zonas seguras** (ex.: a UI do TikTok cobre topo/base) e o mapa de como quebrar um draft em slides.

### Passo 2 — Preparar a pasta de render

Crie a pasta de saída da peça (ex.: `output/<slug>/instagram/arte-ideia-02/`) e **copie `assets/brand.css` para dentro dela**. Os templates referenciam `href="brand.css"` na mesma pasta — sem isso a arte sai sem estilo.

### Passo 3 — Compor os HTMLs

Para cada arte/slide, copie o template adequado de `assets/templates/` e preencha o conteúdo:

- **Carrossel IG:** gere `slide-01.html` (capa, `ig-cover`), `slide-02..N-1.html` (conteúdo/dado, `ig-content`/`ig-data`), `slide-NN.html` (CTA, `ig-cta`). Use o texto do draft, não reescreva o conteúdo — você está diagramando, não redigindo.
- **LinkedIn:** uma imagem (`linkedin-post`) com a tese central; o texto longo fica na legenda, não na imagem.
- **YouTube:** a thumbnail (`youtube-thumbnail`, ≤5 palavras) usando o conceito de thumbnail que veio no draft.
- **TikTok/Reels:** a capa (`tiktok-cover`) com o hook, respeitando a zona segura.

Regras de composição: alterne fundos entre slides para dar ritmo, destaque (`.accent`/azul) só na palavra que carrega a tensão, e respeite os limites de texto por slide das specs. **Dado sempre com `.source`** — coerente com o guardrail de não inventar números.

### Passo 4 — Renderizar

Rode o `render.py` na pasta (renderiza todos os `.html` de uma vez) com a dimensão do canal:

```bash
# carrossel IG (renderiza a pasta inteira)
python scripts/render.py "<pasta-da-peça>" --width 1080 --height 1350

# arte única (LinkedIn / thumbnail / capa) — ajuste width/height pela tabela das specs
python scripts/render.py "<arquivo>.html" --out "<saida>.png" --width 1080 --height 1080
```

`--scale 2` (default) gera saída crisp/retina. Confira: a dimensão passada precisa bater com a classe `canvas--*` do HTML.

### Passo 5 — Conferir e entregar

Abra os PNGs e cheque legibilidade (texto não cortado, contraste, marca correta). Entregue a pasta de artes + os HTMLs (editáveis) junto da legenda já produzida pelo formatter. São **artes prontas para revisão/publicação** — não publicadas automaticamente (isso é o `conteudo-scheduler` / agendador).

## Princípios

- **Diagramar, não reescrever.** O conteúdo e a voz vêm do `multicanal-formatter` (com guardrail OAB já aplicado). Aqui você só dá forma visual — não invente texto nem dado novo.
- **Marca consistente, ritmo variado.** Mesma paleta e fontes sempre; varie fundo/composição para a série não cansar.
- **Editável por princípio.** Entregue os HTMLs junto dos PNGs: o time ajusta uma palavra e re-renderiza em segundos, sem refazer no Canva.
- **Reproduzível.** Mesma entrada → mesma arte. É o que permite escalar produção sem perder identidade.
