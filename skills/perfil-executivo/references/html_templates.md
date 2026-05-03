# HTML Templates — Perfil Executivo

Templates HTML completos para cada tipo de página do documento.

---

## Template: Capa (Página 1)

```html
<div class="page cover-page">
  <!-- Efeito de blob/glow nos cantos -->
  <div class="blob blob-top-right"></div>
  <div class="blob blob-bottom-left"></div>

  <div class="cover-content">
    <!-- Ícone/Logo -->
    <div class="cover-logo">
      <div class="logo-box">
        <!-- SVG do ícone de camadas (padrão) ou logo da empresa -->
        <svg width="60" height="60" viewBox="0 0 60 60" fill="none">
          <rect width="60" height="60" rx="14" fill="url(#logoGrad)"/>
          <path d="M15 22l15-8 15 8-15 8-15-8z" fill="white" opacity="0.9"/>
          <path d="M15 30l15 8 15-8" stroke="white" stroke-width="2.5" fill="none"/>
          <path d="M15 38l15 8 15-8" stroke="white" stroke-width="2" fill="none" opacity="0.6"/>
          <defs>
            <linearGradient id="logoGrad" x1="0" y1="0" x2="60" y2="60">
              <stop offset="0%" stop-color="#7b4fff"/>
              <stop offset="100%" stop-color="#00c9b1"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
    </div>

    <!-- Badge -->
    <div class="cover-badge">EBOOK</div>

    <!-- Título Principal -->
    <h1 class="cover-title">{TITULO_PRINCIPAL}</h1>

    <!-- Linha divisória -->
    <div class="cover-divider"></div>

    <!-- Data -->
    <p class="cover-date">{DATA}</p>
  </div>

  <!-- Rodapé -->
  <div class="cover-footer">{NOME_EMPRESA}</div>
</div>
```

### CSS da Capa
```css
.cover-page {
  background: radial-gradient(ellipse at 70% 20%, #2d1b8e 0%, #0d0a2e 50%),
              radial-gradient(ellipse at 30% 80%, #4a1278 0%, transparent 50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.blob {
  position: absolute;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.3;
}
.blob-top-right { top: -100px; right: -100px; background: #7b4fff; }
.blob-bottom-left { bottom: -100px; left: -100px; background: #4a1278; }
.cover-content { text-align: center; z-index: 1; padding: 60px 40px; }
.logo-box {
  width: 100px; height: 100px;
  background: linear-gradient(135deg, #7b4fff, #00c9b1);
  border-radius: 24px;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 24px;
  box-shadow: 0 20px 60px rgba(123,79,255,0.4);
}
.cover-badge {
  display: inline-block;
  border: 1.5px solid rgba(0,201,177,0.6);
  border-radius: 20px;
  padding: 6px 20px;
  font-size: 11px;
  letter-spacing: 3px;
  color: #00c9b1;
  margin-bottom: 32px;
}
.cover-title {
  font-size: 52px;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 24px;
  line-height: 1.1;
  letter-spacing: -1px;
}
.cover-divider {
  width: 80px; height: 3px;
  background: linear-gradient(90deg, #7b4fff, #00c9b1);
  margin: 0 auto 24px;
  border-radius: 2px;
}
.cover-date { font-size: 13px; color: #a0a0c0; letter-spacing: 1px; margin: 0; }
.cover-footer {
  position: absolute; bottom: 40px; width: 100%;
  text-align: center; font-size: 11px; letter-spacing: 5px;
  color: rgba(160,160,192,0.7); text-transform: uppercase;
}
```

---

## Template: Sumário (Página 2)

```html
<div class="page toc-page">
  <div class="toc-container">
    <h2 class="toc-title">Sumário</h2>
    <div class="toc-list">
      <!-- Repetir para cada seção -->
      <div class="toc-item">
        <span class="toc-number">01</span>
        <span class="toc-name">{TITULO_SECAO}</span>
        <span class="toc-dots"></span>
        <span class="toc-page">{NUMERO_PAGINA}</span>
      </div>
    </div>
  </div>
</div>
```

### CSS do Sumário
```css
.toc-page { background: #0d0a2e; padding: 80px 60px; }
.toc-title { font-size: 42px; font-weight: 800; margin-bottom: 48px; color: #fff; }
.toc-item {
  display: flex; align-items: center; gap: 16px;
  padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.06);
}
.toc-number { font-size: 13px; font-weight: 700; color: #00c9b1; min-width: 32px; }
.toc-name { font-size: 15px; color: #e0e0f0; flex: 1; }
.toc-dots { flex: 1; border-bottom: 1px dotted rgba(255,255,255,0.15); margin: 0 8px; }
.toc-page { font-size: 13px; color: #7b4fff; font-weight: 600; }
```

---

## Template: Página de Conteúdo

```html
<div class="page content-page">
  <!-- Número decorativo de fundo -->
  <div class="section-num-bg">{NUMERO_SECAO}</div>

  <div class="content-container">
    <!-- Cabeçalho da seção -->
    <div class="section-header">
      <div class="section-badge">
        <span class="section-num">{NUMERO_SECAO}</span>
      </div>
      <h2 class="section-title">{EMOJI} {TITULO_SECAO}</h2>
    </div>

    <!-- Subtítulo/intro -->
    <p class="section-intro">{INTRODUCAO_SECAO}</p>

    <!-- Subtítulo de bloco -->
    <h3 class="block-title">{TITULO_BLOCO}</h3>

    <!-- Parágrafo de texto -->
    <p class="body-text">{TEXTO}</p>

    <!-- Lista com check -->
    <ul class="check-list">
      <li class="check-item">
        <span class="check-icon">✓</span>
        <span class="check-text"><strong>{ITEM_BOLD}:</strong> {DESCRICAO}</span>
      </li>
    </ul>

    <!-- Card de conteúdo -->
    <div class="content-card">
      <h4 class="card-title">{TITULO_CARD}</h4>
      <p class="card-text">{CONTEUDO_CARD}</p>
    </div>
  </div>

  <!-- Rodapé -->
  <div class="page-footer">
    <span class="footer-brand">{NOME_EMPRESA}</span>
    <span class="footer-page">{NUMERO_PAGINA}</span>
  </div>
</div>
```

### CSS de Conteúdo
```css
.content-page { background: #0d0a2e; padding: 60px 60px 80px; position: relative; }
.section-num-bg {
  position: absolute; top: 20px; right: 40px;
  font-size: 140px; font-weight: 900; color: rgba(123,79,255,0.06);
  pointer-events: none; line-height: 1; z-index: 0;
}
.content-container { position: relative; z-index: 1; }
.section-header { display: flex; align-items: center; gap: 20px; margin-bottom: 24px; }
.section-badge {
  width: 48px; height: 48px; border-radius: 12px;
  background: linear-gradient(135deg, #7b4fff, #00c9b1);
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 18px; color: white; flex-shrink: 0;
}
.section-title { font-size: 30px; font-weight: 800; color: #fff; margin: 0; }
.section-intro { font-size: 15px; color: #a0a0c0; line-height: 1.7; margin-bottom: 32px; }
.block-title {
  font-size: 18px; font-weight: 700; color: #00c9b1;
  border-left: 3px solid #7b4fff; padding-left: 14px; margin: 28px 0 16px;
}
.body-text { font-size: 14px; color: #c0c0d8; line-height: 1.75; margin-bottom: 16px; }
.check-list { list-style: none; padding: 0; margin: 0; }
.check-item { display: flex; gap: 12px; margin-bottom: 12px; }
.check-icon { color: #00c9b1; font-weight: 700; font-size: 14px; flex-shrink: 0; margin-top: 2px; }
.check-text { font-size: 14px; color: #c0c0d8; line-height: 1.6; }
.content-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px; padding: 20px 24px; margin: 20px 0;
}
.card-title { font-size: 15px; font-weight: 700; color: #fff; margin: 0 0 8px; }
.card-text { font-size: 13px; color: #a0a0c0; margin: 0; line-height: 1.65; }
.page-footer {
  position: absolute; bottom: 24px; left: 60px; right: 60px;
  display: flex; justify-content: space-between; align-items: center;
  border-top: 1px solid rgba(255,255,255,0.08); padding-top: 16px;
  font-size: 11px; letter-spacing: 2px; color: rgba(160,160,192,0.5);
}
```

---

## Template: Encarte de Oferta

```html
<div class="page offer-page">
  <div class="blob blob-center"></div>
  <div class="offer-content">
    <div class="offer-badge">✦ OFERTA EXCLUSIVA ✦</div>
    <h2 class="offer-title">{TITULO_OFERTA}</h2>
    <p class="offer-desc">{DESCRICAO_PRODUTO}</p>
    <a class="offer-btn">{TEXTO_CTA} →</a>
    <div class="offer-discount">
      <span class="discount-pct">{DESCONTO}</span>
      <span class="discount-label">{LABEL_DESCONTO}</span>
      <div class="discount-bonus">{BONUS}</div>
    </div>
    <div class="qr-placeholder">
      <div class="qr-box">[QR]</div>
      <p class="qr-label">Escaneie o QR Code ou clique no botão acima</p>
    </div>
    <div class="offer-urgency">⏰ OFERTA POR TEMPO LIMITADO</div>
  </div>
</div>
```

### CSS da Oferta
```css
.offer-page {
  background: radial-gradient(ellipse at 50% 50%, #1a1060 0%, #0d0a2e 70%);
  display: flex; align-items: center; justify-content: center; text-align: center;
}
.blob-center { top: 50%; left: 50%; transform: translate(-50%,-50%); background: #7b4fff; }
.offer-badge {
  font-size: 11px; letter-spacing: 3px; color: #00c9b1;
  border: 1px solid rgba(0,201,177,0.4); border-radius: 20px;
  padding: 6px 20px; display: inline-block; margin-bottom: 28px;
}
.offer-title { font-size: 42px; font-weight: 800; color: #fff; line-height: 1.15; margin-bottom: 20px; }
.offer-desc { font-size: 15px; color: #a0a0c0; max-width: 480px; margin: 0 auto 32px; line-height: 1.65; }
.offer-btn {
  display: inline-block; padding: 16px 40px;
  background: linear-gradient(135deg, #7b4fff, #00c9b1);
  border-radius: 8px; font-size: 13px; font-weight: 700;
  letter-spacing: 2px; color: white; text-decoration: none; margin-bottom: 24px;
}
.offer-discount {
  background: rgba(123,79,255,0.15); border: 1px solid rgba(123,79,255,0.3);
  border-radius: 8px; padding: 12px 24px; display: inline-block; margin-bottom: 32px;
}
.discount-pct { font-size: 22px; font-weight: 800; color: #ffd700; }
.discount-label { font-size: 14px; color: #c0c0d8; margin-left: 8px; }
.discount-bonus { font-size: 12px; color: #a0a0c0; margin-top: 4px; }
.qr-box {
  width: 100px; height: 100px; border: 2px solid rgba(255,255,255,0.15);
  border-radius: 8px; margin: 0 auto 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; color: rgba(255,255,255,0.3);
}
.qr-label { font-size: 12px; color: #6060a0; }
.offer-urgency { font-size: 11px; letter-spacing: 2px; color: rgba(160,160,192,0.5); margin-top: 24px; }
```

---

## Template: Página de Encerramento

```html
<div class="page closing-page">
  <div class="closing-content">
    <div class="logo-box">
      <!-- mesmo SVG da capa -->
    </div>
    <p class="closing-prefix">PRODUZIDO COM</p>
    <h2 class="closing-brand">
      <span class="brand-accent">{NOME_EMPRESA_PARTE1}</span>
      <span class="brand-main"> {NOME_EMPRESA_PARTE2}</span>
    </h2>
    <div class="cover-divider" style="margin: 16px auto;"></div>
    <p class="closing-tagline">{TAGLINE}</p>
  </div>
</div>
```

### CSS do Encerramento
```css
.closing-page {
  background: #050318;
  display: flex; align-items: center; justify-content: center; text-align: center;
}
.closing-prefix { font-size: 11px; letter-spacing: 5px; color: rgba(160,160,192,0.5); margin: 20px 0 8px; }
.closing-brand { font-size: 32px; font-weight: 800; margin: 0; }
.brand-accent { color: #7b4fff; }
.brand-main { color: #00c9b1; }
.closing-tagline { font-size: 13px; color: rgba(160,160,192,0.6); margin: 8px 0 0; }
```
