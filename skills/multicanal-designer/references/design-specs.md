# Specs de design por canal

Dimensões, zonas seguras e o mapa de qual template usar. Todas as artes usam `assets/brand.css` (cores e fontes Horus). Renderize com `scripts/render.py`.

## Dimensões e template

| Canal | Dimensão (px) | Classe canvas | Templates | Escala |
|-------|---------------|---------------|-----------|--------|
| Instagram (carrossel/feed) | 1080 × 1350 | `canvas--ig-vertical` | `ig-cover`, `ig-content`, `ig-data`, `ig-cta` | 2 |
| LinkedIn (imagem do post) | 1080 × 1080 | `canvas--square` | `linkedin-post` | 2 |
| YouTube (thumbnail) | 1280 × 720 | `canvas--yt-thumb` | `youtube-thumbnail` | 2 |
| TikTok/Reels (cover) | 1080 × 1920 | `canvas--vertical` | `tiktok-cover` | 2 |

A dimensão passada ao `render.py` (`--width`/`--height`) **deve bater** com a classe canvas do HTML, senão a arte fica cortada ou com borda.

## Zonas seguras (não deixe nada vital aqui)

- **Instagram carrossel:** a seta de "próximo" cobre a borda direita central; o último slide deve ter CTA claro. Margem segura já embutida na classe `.pad`.
- **TikTok/Reels:** a UI do app cobre ~220px no topo e ~320px na base (legenda, botões, música). O template `tiktok-cover` já recua o conteúdo (`padding:260px 80px 360px`). Nunca ponha texto essencial fora disso.
- **YouTube thumbnail:** o tempo do vídeo aparece no canto inferior direito — evite texto ali.

## Mapa: draft → slides (carrossel Instagram)

Um carrossel tem 6–10 slides. Use os tipos de slide assim:

| Posição | Tipo | Template | Conteúdo |
|---------|------|----------|----------|
| 1 | Capa | `ig-cover` | o gancho (≤8 palavras) com 1 palavra em `.accent` (azul) |
| 2 … N-1 | Conteúdo ou Dado | `ig-content` / `ig-data` | 1 ideia por slide; use `ig-data` quando o slide é um número forte |
| N | CTA | `ig-cta` | fechamento + CTA informativo (salvar/comentar/seguir) |

Cada slide vira um arquivo `slide-01.html`, `slide-02.html`, … na pasta de saída. O `render.py` renderiza a pasta inteira de uma vez.

## Recursos de marca disponíveis no brand.css

- **Fundos:** `bg-purple`, `bg-blue`, `bg-dark`, `bg-light`, `bg-gradient` (purple→dark), `bg-gradient-blue` (purple→blue). Alterne fundos entre slides para dar ritmo (ex.: capa em gradiente, conteúdo em dark, dado em gradient-blue, CTA em purple).
- **Grade digital:** adicione a classe `grid-overlay` ao canvas para a textura de grade neon sutil da marca.
- **Tipografia:** `.title` (Montserrat) com `--xl/--lg/--md`; `.body` (Open Sans) com `--lg/--md`; `.accent` (azul), `.muted`.
- **Componentes:** `.pill` (etiqueta), `.bignum` (número gigante p/ dado), `.footer` + `.handle` + `.slide-num`, `.source` (crédito de fonte).

## Princípios de design (Horus)

- **Um foco por arte.** Capa promete uma coisa; cada slide entrega uma. Slide poluído não é lido.
- **Hierarquia clara.** Título grande (Montserrat 800), corpo menor (Open Sans). O olho deve saber onde pousar primeiro.
- **Destaque com propósito.** Use o azul (`.accent`) na palavra que carrega a tensão — não em tudo.
- **Marca consistente, não engessada.** Mesma paleta e fontes sempre; varie fundo e composição para não ficar repetitivo numa série.
- **Dado sempre com fonte.** Slides de número (`ig-data`) levam `.source` — coerente com o guardrail de não inventar dado.

## Erros comuns

- Dimensão do render ≠ classe canvas → arte cortada. Confira a tabela.
- Texto demais por slide → ilegível no celular. Máx. ~40 palavras (conteúdo) / ~8 (capa).
- `brand.css` em pasta errada → arte sem estilo (fundo branco, fonte serifada). Copie o `brand.css` para a MESMA pasta dos slides e use `href="brand.css"`.
- Esquecer a zona segura do TikTok → texto coberto pela UI do app.
