---
name: ux-premium-audit
description: Auditar e planejar transformação de UX premium para qualquer site. Use para analisar páginas existentes, mapear conteúdo para técnicas de UX premium (progressive disclosure, scroll-driven storytelling, micro-interações), e gerar planos prompt-a-prompt prontos para implementação no Lovable.dev.
---

# UX Premium Audit - Transformação de Experiência

Esta skill fornece um workflow estruturado para transformar qualquer site em uma experiência premium interativa, mantendo 100% do conteúdo existente e aplicando apenas técnicas de UX.

## Workflow Principal

O processo segue 4 etapas principais:

1. **Análise do Site** - Coletar informações sobre a página atual
2. **Mapeamento de Seções** - Mapear conteúdo para técnicas de UX premium
3. **Geração de Plano** - Criar estrutura de fases e prompts
4. **Entrega de Prompts** - Gerar prompts prontos para Lovable.dev

## Como Usar Esta Skill

### Etapa 1: Fornecer Informações do Site

Quando solicitado, forneça:
- **URL do site** ou captura de tela (PDF/imagem)
- **Stack técnico atual** (React, Next.js, WordPress, etc)
- **Objetivo principal** (gerar leads, vender, educar, engajar)
- **Hospedagem e CMS** (Vercel, AWS, Supabase, etc)

### Etapa 2: Análise Automática

Manus irá:
- Analisar a estrutura de seções do site
- Identificar conteúdo a preservar (textos, imagens, métricas, depoimentos)
- Mapear cada seção para técnicas de UX premium apropriadas
- Documentar oportunidades de transformação

### Etapa 3: Geração do Plano

Manus criará um documento com:
- **Mapeamento:** Seção → Técnica de UX → Prompts necessários
- **Fases:** Organização em 4-7 fases de implementação
- **Prompts:** 8-15 prompts específicos e prontos para usar
- **Cronograma:** Estimativa de tempo por fase
- **Métricas:** Objetivos de sucesso (scroll depth, conversão, performance)

### Etapa 4: Usar os Prompts

Copie cada prompt gerado e cole no Lovable.dev. Cada prompt é:
- **Específico:** Direcionado para uma seção ou funcionalidade
- **Contextualizado:** Inclui informações sobre o que foi feito antes
- **Detalhado:** Requisitos técnicos, conteúdo a preservar, responsividade
- **Pronto:** Pode ser usado imediatamente sem modificações

## Técnicas de UX Premium Disponíveis

A skill aplica 8 técnicas principais (consulte `references/ux-premium-techniques.md` para detalhes):

1. **Progressive Disclosure** - Revelar conteúdo sequencialmente
2. **Scroll-Driven Storytelling** - Narrativa guiada pelo scroll
3. **Micro-interações** - Animações funcionais em elementos interativos
4. **Contadores Animados** - Números que animam de 0 até valor final
5. **Carrosséis Interativos** - Componentes com drag e auto-play
6. **Split-Screen Animado** - Layout com dois lados conectados visualmente
7. **Sticky Scroll** - Elemento fixo enquanto conteúdo muda
8. **Design Conversacional** - Interface que simula diálogo (Typebot-style)

## Stack Recomendado

Para melhor resultado, a implementação deve usar:
- **Frontend:** React + Vite + TypeScript
- **Estilização:** Tailwind CSS
- **Animações:** Framer Motion
- **Detecção de Scroll:** Intersection Observer API
- **Backend:** Supabase ou similar para dados dinâmicos

A skill é agnóstica de stack, mas otimizada para React/Framer Motion.

## Estrutura de Fases Padrão

A maioria dos planos segue este padrão:

| Fase | Objetivo | Prompts | Duração |
|------|----------|---------|---------|
| **1** | Preparação (estrutura + animações) | 1-2 | 2-3 dias |
| **2** | Seções críticas (hero, pricing) | 2-3 | 2-3 dias |
| **3** | Seções principais (features, resultados) | 2-4 | 3-4 dias |
| **4** | Seções secundárias (depoimentos, FAQ) | 2-3 | 2-3 dias |
| **5** | Polish (micro-interações globais) | 1-2 | 1-2 dias |
| **6** | Otimização (performance, responsividade) | 1-2 | 1-2 dias |
| **7** | Testes (validação e ajustes) | 1 | 1-2 dias |

**Total estimado:** 12-20 prompts em 14-21 dias

## Preservação de Conteúdo

A skill garante que **100% do conteúdo existente seja preservado**:
- ✅ Todos os textos e títulos
- ✅ Todas as imagens e ícones
- ✅ Todas as métricas e números
- ✅ Todos os depoimentos
- ✅ Todos os CTAs e links
- ✅ Toda a estrutura de navegação

**Apenas a experiência muda**, não o conteúdo.

## Recursos Inclusos

A skill inclui templates e referências reutilizáveis:

- **`templates/site-analysis-template.md`** - Formulário para coletar informações do site
- **`references/ux-premium-techniques.md`** - Guia detalhado de cada técnica (quando usar, como implementar)
- **`references/prompt-generation-workflow.md`** - Workflow para gerar prompts (padrões e exemplos)

Consulte estes arquivos conforme necessário durante o processo.

## Exemplo de Uso

**Entrada:**
- URL: https://exemplo.com.br
- Stack: React + Vite + TypeScript + Tailwind
- Objetivo: Gerar leads
- Seções: Hero, 3 soluções, resultados, pricing, FAQ

**Saída:**
- Análise de 6 seções
- Mapeamento para 8 técnicas de UX premium
- 12 prompts organizados em 6 fases
- Cronograma de 16-18 dias
- Métricas de sucesso definidas

**Próximo passo:**
- Copiar Prompt 1 e colar no Lovable.dev
- Validar output
- Continuar com Prompt 2, 3, etc

## Dicas para Melhor Resultado

1. **Forneça captura completa** - Se possível, PDF ou screenshot de toda a página
2. **Descreva o objetivo** - Quanto mais claro o objetivo, melhor o plano
3. **Mencione stack atual** - Facilita recomendações técnicas
4. **Implemente sequencialmente** - Não tente fazer tudo de uma vez
5. **Valide após cada fase** - Ajuste conforme necessário
6. **Acompanhe métricas** - Rastreie scroll depth, conversão, performance
7. **Itere baseado em feedback** - Usuários reais darão insights valiosos

## Limitações e Considerações

- A skill assume que o conteúdo atual é válido e bem estruturado
- Não faz recomendações sobre mudanças de conteúdo ou estratégia
- Foca em experiência (UX), não em conversão (CRO) diretamente
- Performance final depende da implementação correta dos prompts
- Requer conhecimento técnico para executar os prompts no Lovable.dev

## Próximas Etapas Após Usar Esta Skill

1. Receber plano de implementação com prompts
2. Usar prompts no Lovable.dev para gerar código
3. Testar em dispositivos reais
4. Coletar métricas (scroll depth, conversão, performance)
5. Iterar baseado em dados reais
6. Documentar aprendizados para futuras implementações
