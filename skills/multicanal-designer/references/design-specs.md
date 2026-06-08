# Specs de design — Sistema Horus Hub

Sistema visual canônico (fonte de verdade: `horus-core/docs/estrategia/02-marca/guia-de-marca-horus.md` + o motor `horus_creative_engine.py`). Todas as artes usam `assets/brand.css`. Renderize com `scripts/render.py`.

## Identidade (resumo)

- **Fundo:** dark `#0a0a0f` + 2 glows (roxo topo-direita, azul base-esquerda) + grid sutil 64px.
- **Cores:** roxo `#7c26d9` (CTA/marca), azul `#3b82f6` ("Hub"/destaque), magenta `#a855f7` (início do gradiente). Gradiente de destaque `100deg #a855f7→#3b82f6`; CTA `100deg #7c26d9→#3b82f6`.
- **Fontes:** Space Grotesk (títulos/marca/kicker), Inter (corpo), Montserrat (números).
- **Marca:** emblema + "Horus **Hub**" (Hub azul) no topo. Handle `@horushub.ia`. Tagline "Transformando escritórios de advocac[IA] com IA e Marketing Jurídico".
- **Recurso `[IA]`:** colchete roxo **só** em palavra que já contém "ia" (advocac[IA], estratég[IA]). Nunca em "Hub". Use `<span class="iabr">[<b>IA</b>]</span>`.

## Os 4 estilos (vocabulário do feed)

| Estilo | Template | Composição | Quando usar |
|--------|----------|------------|-------------|
| **default** | `feed-default.html` | kicker + headline + sub + (pill) | manifesto, tese, persona, FAQ |
| **data** | `feed-data.html` | kicker + número gigante (`.bignum`) + headline | estatística forte (ex.: "77%") |
| **mantra** | `feed-mantra.html` | aspas grandes + frase centralizada | bordões de marca |
| **offer** | `feed-offer.html` | kicker + headline + sub + linhas (label/valor) + pill | ecossistema, planos, diagnóstico |

Destaque no título: envolva a palavra-chave (a que carrega a tensão) em `<span class="hl">…</span>` (gradiente). Use com parcimônia — 1 trecho por título.

## Dimensões por canal

| Canal | Dimensão (px) | Classe canvas | Template | Escala |
|-------|---------------|---------------|----------|--------|
| Instagram (feed/carrossel) | 1080 × 1350 | `canvas--feed` | os 4 estilos | 1–2 |
| LinkedIn (imagem do post) | 1080 × 1080 | `canvas--square` | `linkedin-square.html` | 1–2 |
| YouTube (thumbnail) | 1280 × 720 | `canvas--yt-thumb` | `youtube-thumb.html` | 1–2 |
| TikTok/Reels (cover) | 1080 × 1920 | `canvas--vertical` | `tiktok-cover.html` | 1–2 |

A dimensão passada ao `render.py` (`--width/--height`) **deve bater** com a classe `canvas--*`. O motor canônico usa `--scale 1`; use `--scale 2` se quiser saída retina.

## Carrossel (IG)

Um carrossel = vários slides, cada um um arquivo (`slide-01.html`…). Alterne estilos para dar ritmo (capa em `default`, um slide `data`, fechamento com pill). Marque o último com CTA informativo. A afford. `arraste →` (classe `.swipe`) vai no rodapé dos slides que pedem continuação.

## Zonas seguras

- **TikTok/Reels:** UI cobre ~220px topo / ~320px base — o template já recua. Nada essencial fora disso.
- **YouTube:** o tempo do vídeo cobre o canto inferior direito.
- **Instagram carrossel:** a seta de "próximo" fica na borda direita central.

## Emblema (asset de marca)

O `brand.css` desenha um **hexágono CSS** (`.emblem-ph`) como placeholder público. Para a arte **real da Horus**, troque por `<img class="emblem" src="emblema.png">` apontando para o emblema oficial (asset privado em `horus-core/docs/estrategia/02-marca/assets/`). Não commite o logo proprietário no repo público.

## Produção Horus: prefira o motor canônico

Para gerar arte Horus de produção (feed 1080×1350, os 4 estilos, emblema real), **use o motor** `horus-core/docs/estrategia/05-criativos-conteudo-gtm/_criativos/horus_creative_engine.py` (`render_criativos(items, out_dir)`) — é a fonte de verdade do visual, já com o emblema oficial. Este `brand.css`/templates são o tema público equivalente, para uso fora do ambiente Horus ou quando o motor não estiver acessível.

## Erros comuns

- Dimensão do render ≠ classe canvas → arte cortada.
- `brand.css` em pasta errada → arte sem estilo (fundo branco). Copie para a MESMA pasta dos slides.
- `[IA]` em palavra sem "ia" (ex.: "Hub") — errado; é recurso semântico, não decorativo.
- Texto demais por slide → ilegível no celular.
