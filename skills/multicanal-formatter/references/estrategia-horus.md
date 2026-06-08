# Estratégia Horus — ponteiro para o pacote privado

> **Separação de IP (ADR thoth público / Horus privado):** este arquivo, no repo público,
> NÃO contém a estratégia comercial sensível (preços, value ladder, copy dos criativos,
> funil GTM). Ele aponta para o pacote **privado** no horus-core e dá só o esqueleto
> não-sensível. Ao produzir conteúdo **Horus**, leia o pacote privado.

## Onde está a estratégia canônica (privado)

`horus-core/docs/estrategia/` — comece pelo índice do pipeline:

- **`PIPELINE-CONFIG.md`** — índice que liga personas→mensagem, value ladder→CTA, pilares, exemplos campeões e cadência. **Leia este primeiro.**
- `02-marca/guia-de-marca-horus.md` — voz, mantras, [IA], naming.
- `03-pesquisa-mercado-posicionamento/` — posicionamento, ICP, Provimento 205.
- `04-ofertas-value-ladder/ofertas-value-ladder.md` — degraus + preços + CTAs.
- `05-criativos-conteudo-gtm/` — 4 pilares, calendário 30d, e os **12 criativos campeões** (`_criativos/`).

Se o horus-core não estiver acessível (uso fora do ambiente Horus), produza com a voz de `voz-horus-oab.md` e sinalize que a estratégia comercial detalhada não foi carregada.

## Esqueleto não-sensível (para orientar o ângulo)

**Personas (ICP)** — angule a peça para uma:
- **Advogado solo** — dor: captar sem virar "vendedor", sem tempo. Mensagem: "capte e atenda com IA sem perder a mão".
- **Boutique (2–10)** — dor: previsibilidade de leads + organizar operação.
- **Banca média** — dor: eficiência + governança/LGPD/sigilo.

**Pilares de conteúdo** (toda peça serve a um):
- 🎓 **Educar** (~40%) — entrada de massa (ex.: usar IA dentro da OAB, desmistificar).
- 🤖 **Demonstrar** (~25%) — prova de produto (Estagiário citando fonte, JurisLab).
- ⚙️ **Processo** (~20%) — autoridade + conformidade como venda (método, funil ético).
- 🏛️ **Autoridade** (~15%) — tese, mantras, portfólio.

**Exemplos campeões** = os 12 criativos D01–D28 (ver refs de canal e o `_criativos/`). Imite estrutura e voz deles — são peças reais validadas por OAB.

**Funil / value ladder / preços:** estão **só no pacote privado**. Não os reproduza no público; leia de `PIPELINE-CONFIG.md` / `ofertas-value-ladder.md` quando for produzir oferta.
