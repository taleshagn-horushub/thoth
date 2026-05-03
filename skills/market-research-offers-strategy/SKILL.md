---
name: market-research-offers-strategy
description: "Realiza pesquisa aprofundada de mercado (Wide Research) de competidores e cria estratégia completa de ofertas escaláveis (Value Ladder). Use para: analisar concorrentes, identificar falhas no mercado, estruturar pacotes produtizados e criar estratégias de precificação."
license: Complete terms in LICENSE.txt
---

# Market Research & Offers Strategy

Esta skill guia o processo de realização de uma pesquisa de mercado em larga escala (Wide Research) e a subsequente criação de uma estratégia de ofertas escaláveis baseada nos insights coletados.

## Fluxo de Trabalho

O processo é dividido em três etapas principais:

### 1. Wide Research (Pesquisa de Competidores)

1. **Identificar Competidores:** Solicite ao usuário ou pesquise uma lista de 10 a 15 principais competidores no nicho desejado (agências, consultorias, SaaS, etc.).
2. **Executar Pesquisa em Paralelo:** Utilize a ferramenta `map` para pesquisar todos os competidores simultaneamente.
   - Use o template de prompt localizado em `templates/wide_research_prompt.txt` para guiar a extração de dados.
   - Extraia: descrição, modelo de negócio, ofertas/planos, preços, público-alvo, diferenciais, pontos fracos e insights de oportunidade.
3. **Consolidar Dados:** Analise os resultados do JSON gerado e crie um documento de insights (`insights-competidores.md`).
   - Identifique padrões: O que está funcionando? (ex: produtização, IA).
   - Identifique falhas: Quais são as maiores reclamações? (ex: falta de transparência, suporte ruim).

### 2. Criação da Estratégia de Ofertas (Value Ladder)

1. **Ler Metodologia:** Leia o arquivo `references/metodologia_ofertas.md` para entender os conceitos de Value Ladder, posicionamento "Anti-Agência" e características de ofertas irresistíveis.
2. **Definir Posicionamento:** Com base nas falhas identificadas na pesquisa, defina um posicionamento que ataque diretamente as dores do mercado (ex: se o mercado esconde preços, a estratégia deve focar em transparência radical).
3. **Criar Ofertas Core (Alto Ticket):** Desenvolva de 3 a 5 ofertas principais.
   - Defina: Nome, Posicionamento, Preço, Escopo Incluído e Por que Funciona (baseado nos insights).
   - Salve em um documento (ex: `5-ofertas-core.md`).
4. **Criar Ofertas Front-End (Ticket Baixo):** Desenvolva de 5 a 10 ofertas de entrada.
   - Foco: Alta percepção de valor, baixa complexidade de entrega (menos de 4h) e upsell natural para as ofertas Core.
   - Defina: Nome, Preço, O que é, Entregáveis e Por que Funciona.
   - Salve em um documento (ex: `10-ofertas-ticket-baixo.md`).

### 3. Entrega do Relatório Final

1. **Consolidar Estratégia:** Crie um relatório final abrangente (`estrategia-completa-final.md`) que una todas as partes:
   - Resumo dos insights do mercado.
   - O novo posicionamento estratégico.
   - A Value Ladder completa (Ofertas Core + Front-End).
   - A jornada do cliente (como ele flui das ofertas de ticket baixo para as de alto ticket).
   - Projeção financeira conservadora.
   - Próximos passos imediatos para implementação.
2. **Entregar ao Usuário:** Entregue todos os documentos gerados ao usuário, explicando brevemente a lógica por trás da estratégia.

## Recursos Inclusos

### references/
- **metodologia_ofertas.md** - Guia detalhado sobre Value Ladder, posicionamento "Anti-Agência" e características de ofertas irresistíveis.

### templates/
- **wide_research_prompt.txt** - Template de prompt para guiar a extração de dados de competidores durante a pesquisa paralela.
