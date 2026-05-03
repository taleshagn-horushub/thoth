# Técnicas de UX Premium - Guia de Referência

## 1. Progressive Disclosure (Revelação Progressiva)

**O que é:** Revelar conteúdo em etapas lógicas, reduzindo sobrecarga cognitiva.

**Quando usar:**
- Hero sections com múltiplos elementos
- Listas longas de benefícios
- Seções com muita informação

**Como implementar:**
- Elementos entram sequencialmente (stagger effect)
- Delays entre 0.1s e 0.3s
- Easing: easeOut para suavidade
- Duração: 0.4s a 0.8s por elemento

**Exemplo:**
```
Título entra (delay: 0s)
  ↓ (0.2s depois)
Subtítulo entra
  ↓ (0.2s depois)
Benefícios entram (um por um)
  ↓ (0.2s depois)
CTA entra
```

**Ferramentas:** Framer Motion, GSAP, AOS

---

## 2. Scroll-Driven Storytelling

**O que é:** Usar o scroll como motor de uma narrativa, ativando animações conforme o usuário desce.

**Quando usar:**
- Páginas longas com múltiplas seções
- Quando há uma progressão lógica (Problema → Solução → Resultados)
- Para manter engajamento durante scroll

**Como implementar:**
- Intersection Observer API para detectar visibilidade
- Animar elementos quando entram no viewport
- Usar transições suaves entre seções
- Adicionar indicador visual de progresso (scroll bar, dots)

**Exemplo:**
```
Seção 1 visível → Anima entrada
  ↓ (scroll)
Seção 2 visível → Anima entrada
  ↓ (scroll)
Seção 3 visível → Anima entrada
```

**Ferramentas:** Intersection Observer, Framer Motion, GSAP

---

## 3. Micro-interações com Propósito

**O que é:** Animações pequenas que fornecem feedback imediato e guiam a atenção.

**Quando usar:**
- Botões (CTAs)
- Cards
- Links
- Ícones
- Inputs de formulário

**Como implementar:**

### Botões
```
Hover: glow + scale(1.05) + shadow aumenta
Click: scale(0.95) + feedback visual
Active: cor muda
Disabled: opacity reduzida
```

### Cards
```
Hover: shadow aumenta + scale(1.02)
Hover: cor de fundo muda ligeiramente
Hover: ícone pulsa ou rotate
```

### Ícones
```
Hover: rotate(10-20deg) + scale(1.2)
Hover: glow effect (para ícones neon)
Hover: cor muda
```

**Duração:** 0.2s a 0.3s (rápido)
**Easing:** easeOut ou easeInOut

**Ferramentas:** Framer Motion, CSS transitions, GSAP

---

## 4. Contadores Animados

**O que é:** Números que animam de 0 até o valor final, criando impacto visual.

**Quando usar:**
- Métricas de impacto (+300%, 50+, etc)
- Resultados quantificáveis
- Estatísticas de sucesso

**Como implementar:**
```
Quando seção fica visível:
  - Iniciar contador em 0
  - Animar até valor final (duração: 2s)
  - Easing: easeOut
  - Ao final: adicionar checkmark animado
```

**Exemplo:**
```
0 → 50 → 100 → 150 → 200 → 250 → 300 ✓
```

**Ferramentas:** Framer Motion, react-countup, GSAP

---

## 5. Carrosséis Interativos

**O que é:** Componentes que permitem arrastar (drag) ou navegação automática.

**Quando usar:**
- Depoimentos
- Cursos/produtos
- Portfólio
- Casos de sucesso

**Como implementar:**
```
Funcionalidades:
- Drag/swipe para navegar
- Auto-play a cada 5s (pause ao hover)
- Indicadores de página (dots)
- Transição suave (fade + slide)
- Responsivo (1 item mobile, 3 items desktop)
```

**Ferramentas:** Embla Carousel, Framer Motion, Slick

---

## 6. Split-Screen Animado

**O que é:** Layout com dois lados que animam juntos, conectando visualmente dois conceitos.

**Quando usar:**
- Problema vs Solução
- Antes vs Depois
- Dois user personas
- Feature comparison

**Como implementar:**
```
Lado esquerdo: slideInFromLeft
Lado direito: slideInFromRight
Linha conectora: strokeDasharray animation
Ao final: checkmark animado
```

**Responsividade:**
- Desktop: 50/50 split
- Mobile: Stack vertical (um acima do outro)

**Ferramentas:** Framer Motion, SVG animations, GSAP

---

## 7. Sticky Scroll

**O que é:** Um elemento fica fixo enquanto o conteúdo ao lado muda.

**Quando usar:**
- Features com mockups (mockup fica fixo, texto muda)
- Demonstrações de produto
- Comparações

**Como implementar:**
```
Elemento sticky (position: sticky)
Conforme scroll:
  - Detectar qual seção está visível
  - Mudar conteúdo ao lado
  - Animar transição (fade + scale)
```

**Responsividade:**
- Desktop: Usa sticky
- Mobile: Stack vertical (sem sticky)

**Ferramentas:** CSS position: sticky, Intersection Observer, Framer Motion

---

## 8. Design Conversacional (Typebot-Style)

**O que é:** Interface que simula um diálogo, guiando o usuário passo a passo.

**Quando usar:**
- FAQs
- Formulários longos
- Onboarding
- Fluxos de decisão

**Como implementar:**
```
Pergunta 1 aparece
  ↓ (usuário interage)
Resposta aparece com animação
  ↓ (usuário clica "próxima")
Pergunta 2 aparece (pergunta anterior sai)
```

**Animações:**
- Pergunta entra: slideDown + fadeIn
- Resposta entra: fadeIn (com delay)
- Transição: slideUp (pergunta sai) + slideDown (próxima entra)

**Ferramentas:** Framer Motion, React state management

---

## Padrão de Cores Recomendado (Horus Hub)

```
Primária: Roxo (#8B5CF6)
Secundária: Ciano (#06B6D4)
Fundo: Azul escuro (#0F172A)
Texto: Branco/Cinza claro
Acentos: Verde (#10B981)
```

**Gradientes:**
- Roxo → Ciano
- Ciano → Verde
- Verde → Roxo

---

## Performance e Acessibilidade

### Performance
- Lazy load de imagens
- Code splitting por seção
- Memoização de componentes
- GPU acceleration (transform, opacity)
- Remover animações em prefers-reduced-motion

### Acessibilidade
- ARIA labels em elementos interativos
- Contrast WCAG AA mínimo
- Keyboard navigation (Tab, Enter, Escape)
- Screen reader compatibility
- Sem animações que causem epilepsia (flashes > 3/s)

### Métricas
- Lighthouse score > 90
- LCP < 2.5s
- FID < 100ms
- CLS < 0.1

---

## Checklist de Implementação

- [ ] Progressive disclosure no hero
- [ ] Scroll-triggered animations em todas as seções
- [ ] Micro-interações em botões e cards
- [ ] Contadores animados para métricas
- [ ] Carrosséis para depoimentos/cursos
- [ ] Split-screen para problema/solução
- [ ] Sticky scroll (se aplicável)
- [ ] Design conversacional (FAQ)
- [ ] Responsividade em todos os breakpoints
- [ ] Performance otimizada (Lighthouse > 90)
- [ ] Acessibilidade testada
- [ ] Analytics implementado
- [ ] Testes em dispositivos reais
