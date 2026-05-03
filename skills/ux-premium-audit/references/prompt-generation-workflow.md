# Workflow: Geração de Prompts Prompt-a-Prompt

## Visão Geral

Este workflow transforma uma análise de site em um plano de implementação com prompts específicos prontos para usar no Lovable.dev.

## Etapas do Workflow

### 1. Análise do Site (Input)

**Coleta:**
- URL do site
- Screenshot ou PDF da página
- Stack técnico atual
- Objetivo principal
- Conteúdo a preservar

**Output:** Documento de análise preenchido

### 2. Mapeamento de Seções

**Tarefa:** Mapear cada seção do site para técnicas de UX premium.

**Exemplo:**
```
Seção: Hero
Conteúdo: Título, subtítulo, métricas, depoimento, CTA
Técnica: Progressive Disclosure
Prompts necessários: 1 (Hero com fade-in sequencial)

Seção: Soluções (3 cards)
Conteúdo: 3 soluções com descrição
Técnica: Scroll-triggered animations + Split-screen
Prompts necessários: 2 (Ecosystem + Split-screen para cada solução)
```

### 3. Estrutura de Fases

**Padrão de organização:**

| Fase | Objetivo | Prompts | Duração |
|------|----------|---------|---------|
| 1 | Preparação | 1-2 | 2-3 dias |
| 2 | Seções críticas | 3-5 | 3-5 dias |
| 3 | Seções secundárias | 6-10 | 4-6 dias |
| 4 | Polish | 11-14 | 3-5 dias |

### 4. Template de Prompt

Cada prompt segue este template:

```
Contexto: [Situação atual, o que foi feito antes]

Tarefa: [O que fazer, com detalhes específicos]

Requisitos técnicos:
- [Tecnologia 1]
- [Tecnologia 2]
- [Considerações de performance]

Mantenha EXATAMENTE:
- [Conteúdo a preservar]
- [Dados a manter]
```

### 5. Geração de Prompts

**Processo:**

1. **Prompt de Preparação (Prompts 1-2)**
   - Estrutura de componentes
   - Sistema de animações

2. **Prompts de Seções (Prompts 3-N)**
   - Um prompt por seção ou grupo de seções
   - Incluir técnicas específicas
   - Manter conteúdo existente

3. **Prompts de Polish (Prompts N+1 até final)**
   - Micro-interações globais
   - Performance e responsividade
   - Testes e validação

### 6. Estrutura de Saída

**Documento final inclui:**

```
# Plano de Implementação - [Nome do Site]

## Visão Geral
- Objetivo
- Stack
- Cronograma

## Mapeamento: Conteúdo → UX Premium
[Tabela de seções e técnicas]

## Fases de Implementação

### Fase 1: Preparação
#### Prompt 1: [Título]
[Conteúdo do prompt]

#### Prompt 2: [Título]
[Conteúdo do prompt]

### Fase 2: [Seções]
#### Prompt 3: [Título]
[Conteúdo do prompt]

...

## Métricas de Sucesso
[Tabela de métricas]

## Cronograma
[Tabela de fases e durações]
```

---

## Padrões de Prompts por Técnica

### Progressive Disclosure
```
Contexto: [Seção atual]

Tarefa: Refatore [Componente] para revelar elementos sequencialmente:
1. [Elemento 1] entra com fadeInUp (delay: 0s)
2. [Elemento 2] entra com fadeInUp (delay: 0.2s)
3. [Elemento 3] entra com fadeInUp (delay: 0.4s)

Mantenha EXATAMENTE:
- [Conteúdo a preservar]
```

### Scroll-Triggered Animations
```
Contexto: [Seção atual]

Tarefa: Refatore [Componente] para animar quando entra no viewport:
1. Quando a seção fica visível:
   - Título entra com fadeInUp
   - Cada [elemento] entra com fadeInUp + stagger

2. Micro-interações:
   - Hover: [efeito específico]

Mantenha EXATAMENTE:
- [Conteúdo a preservar]
```

### Contadores Animados
```
Contexto: [Seção com métricas]

Tarefa: Implemente contadores animados:
1. Quando a seção fica visível, números animam de 0 até o valor final
2. Duração: 2 segundos
3. Ao final: checkmark animado aparece

Mantenha EXATAMENTE:
- [Valores das métricas]
- [Labels]
```

### Carrosséis Interativos
```
Contexto: [Seção com múltiplos items]

Tarefa: Implemente carrossel interativo:
1. Funcionalidades:
   - Drag/swipe para navegar
   - Auto-play a cada 5s (pause ao hover)
   - Indicadores de página (dots)
   - Transição suave (fade + slide)

2. Responsividade:
   - Desktop: [N] items visíveis
   - Mobile: 1 item visível

Mantenha EXATAMENTE:
- [Conteúdo dos items]
```

---

## Dicas para Geração Eficiente

1. **Agrupe seções similares** - Se há 3 seções com o mesmo padrão, crie um prompt genérico
2. **Reutilize componentes** - Componentes de micro-interações podem ser aplicados globalmente
3. **Priorize seções críticas** - Hero, pricing, CTAs primeiro
4. **Deixe polish por último** - Performance e acessibilidade vêm após funcionalidades
5. **Teste incrementalmente** - Valide após cada fase, não apenas no final

---

## Exemplo Completo: Site de 5 Seções

```
Site: E-commerce de Cursos

Seção 1: Hero
- Técnica: Progressive Disclosure
- Prompts: 1

Seção 2: Cursos (3 cards)
- Técnica: Scroll-triggered + Carrossel
- Prompts: 2

Seção 3: Resultados (4 métricas)
- Técnica: Contadores animados
- Prompts: 1

Seção 4: Depoimentos (3 cards)
- Técnica: Carrossel interativo
- Prompts: 1

Seção 5: Pricing (3 planos)
- Técnica: Hover effects + Destaque
- Prompts: 1

Total: 6 prompts + 2 de polish = 8 prompts
Duração estimada: 10-15 dias
```
