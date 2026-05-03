---
name: architecture-diagram
description: "Gera diagramas de arquitetura de sistemas em formato Mermaid. Use para: criar representações visuais de arquiteturas de software, fluxos de dados, infraestrutura em nuvem e topologias de rede usando a sintaxe Mermaid."
---

# Architecture Diagram

## Overview

Esta skill orienta a criação de diagramas de arquitetura de sistemas claros, precisos e bem estruturados utilizando a sintaxe Mermaid. Ela define padrões de design, melhores práticas e exemplos para garantir que os diagramas gerados sejam fáceis de entender e manter.

## Diretrizes de Design

Ao criar diagramas de arquitetura em Mermaid, siga estas diretrizes:

1. **Escolha o Tipo de Diagrama Adequado**:
   - Use `graph` (ou `flowchart`) para arquiteturas gerais, fluxos de dados e topologias.
   - Use `sequenceDiagram` para interações entre componentes ao longo do tempo.
   - Use `classDiagram` para modelos de dados e estruturas orientadas a objetos.

2. **Organização e Layout**:
   - Para `flowchart`, prefira a direção `TD` (Top-Down) ou `LR` (Left-Right) dependendo da complexidade. `LR` geralmente funciona melhor para pipelines de dados, enquanto `TD` é bom para hierarquias.
   - Agrupe componentes relacionados usando `subgraph`. Isso ajuda a organizar visualmente o diagrama (ex: separar Frontend, Backend, Banco de Dados, ou zonas de rede).

3. **Nomenclatura e Estilização**:
   - Use IDs curtos e descritivos para os nós (ex: `api`, `db`, `ui`).
   - Adicione rótulos claros aos nós usando a sintaxe `id[Rótulo]`.
   - Adicione rótulos às arestas quando a relação não for óbvia (ex: `api -->|Lê/Escreve| db`).
   - Use estilos (`style` ou `classDef`) para diferenciar tipos de componentes (ex: bancos de dados em uma cor, serviços externos em outra).

## Exemplos de Arquitetura

Veja exemplos de arquiteturas comuns no arquivo de referência:
Consulte [references/examples.md](references/examples.md) para ver exemplos de diagramas Mermaid para arquiteturas web em três camadas, microsserviços e pipelines de dados.

## Fluxo de Trabalho

1. **Análise de Requisitos**: Entenda os componentes do sistema, suas responsabilidades e como eles interagem.
2. **Esboço Inicial**: Identifique os principais nós e agrupamentos (subgraphs).
3. **Desenvolvimento do Código Mermaid**: Escreva o código seguindo as diretrizes acima.
4. **Revisão**: Verifique se o diagrama representa com precisão a arquitetura e se é visualmente claro.
5. **Renderização**: Se necessário, use a ferramenta `manus-render-diagram` para converter o código Mermaid em uma imagem PNG.
