---
name: lovable-feature-research
description: "Realiza pesquisa aprofundada e cria planos de implementação para novas funcionalidades na plataforma Lovable.dev da Horus Hub. Use para: pesquisar mercado/concorrentes, listar funcionalidades com aplicações de negócio e gerar planos de implementação prompt-a-prompt."
---

# Lovable Feature Research & Implementation

Esta skill guia o agente na pesquisa, análise e planejamento de implementação de novas funcionalidades para a plataforma Lovable.dev da Horus Hub.

## Quando Usar

Use esta skill quando o usuário solicitar a pesquisa ou implementação de uma nova funcionalidade para a Lovable.dev, fornecendo um sumário executivo ou descrição do negócio e da necessidade.

## Fluxo de Trabalho

Siga este processo de 6 etapas para entregar os resultados esperados:

1.  **Análise do Contexto**: Leia atentamente o sumário executivo fornecido pelo usuário (Descrição do Negócio, Contexto da Funcionalidade, Critérios de Sucesso, Restrições).
2.  **Pesquisa Abrangente**: Use ferramentas de busca para investigar mercado, concorrentes, tendências de UX/UI e tecnologias.
3.  **Síntese**: Identifique padrões e oportunidades para a Horus Hub.
4.  **Criação de Documentos**: Gere os 3 documentos obrigatórios em Markdown (ver seção "Saídas").
5.  **Geração de Prompts**: Crie a sequência de prompts de implementação focada na stack da Lovable.dev.
6.  **Revisão**: Garanta que tudo esteja em Português do Brasil e focado em UX/Design.

## Saídas (3 Documentos)

O agente deve gerar e entregar os seguintes arquivos Markdown:

### 1. Pesquisa de Negócio (`1_pesquisa_negocio.md`)
- **Análise de Mercado**: Tamanho, segmentos, oportunidades.
- **Análise Competitiva**: Concorrentes diretos/indiretos, pontos fortes/fracos.
- **Tendências**: Tecnologias emergentes e UX.
- **Benchmarking**: Comparativo de funcionalidades.
- **Recomendações**: Estratégias para a Horus Hub.

### 2. Lista de Funcionalidades (`2_funcionalidades.md`)
- Lista de funcionalidades identificadas.
- Descrição concisa e ferramentas de referência.
- **Aplicação para Horus Hub**: Como agrega valor ao negócio.
- **Prioridade**: Alta/Média/Baixa com justificativa.

### 3. Plano de Implementação (`3_plano_implementacao.md`)
- **Visão Geral**: Objetivo e valor.
- **Estrutura do Projeto**: Organização de módulos/componentes.
- **Prompts Detalhados**: Sequência "prompt-a-prompt" para o usuário copiar e colar, cobrindo:
    - Design/UX (wireframes, fluxos).
    - Frontend (React, TypeScript, TailwindCSS).
    - Backend (APIs, Drizzle, MySQL/TiDB, Manus-Oauth).
    - Testes e Otimizações.
- **Melhorias**: Sugestões de UX/Design além do básico.

## Stack Tecnológica da Lovable.dev

Todas as recomendações técnicas e prompts devem utilizar estritamente:
- **Frontend**: React, TypeScript, TailwindCSS.
- **Backend/DB**: Drizzle ORM, MySQL ou TiDB.
- **Auth**: Manus-Oauth.
- **Foco**: UX/Design Centric.

## Instruções Adicionais

- **Idioma**: Português do Brasil.
- **Citações**: Use links para referências externas.
- **Iteração**: O plano de implementação deve ser modular e iterativo.
