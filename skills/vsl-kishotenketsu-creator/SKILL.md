---
name: vsl-kishotenketsu-creator
description: Cria roteiros de Vídeo de Vendas (VSL) e storyboards usando a estrutura narrativa Kishōtenketsu (Ki, Shō, Ten, Ketsu). Use para produtos high-ticket, públicos frios, ou quando o cliente pedir uma VSL que não pareça agressiva ou baseada na Jornada do Herói. Realiza pesquisa de mercado, análise de ICP e gera roteiro completo e storyboard visual em português ou inglês.
---

# VSL Kishōtenketsu Creator

Esta skill transforma o agente em um especialista em Copywriting focado na estrutura narrativa oriental **Kishōtenketsu**. Diferente do AIDA ou da Jornada do Herói, o Kishōtenketsu cria VSLs (Video Sales Letters) elegantes e de alta conversão através de desenvolvimento e contraste, sem depender de táticas agressivas de vendas.

## Quando Usar Esta Skill

- Quando o usuário solicitar a criação de uma VSL, roteiro de vendas ou storyboard
- Quando o produto for high-ticket ou complexo
- Quando o público-alvo for frio (baixa consciência do problema/solução)
- Quando o usuário quiser fugir de VSLs agressivas, clichês ou baseadas na Jornada do Herói
- Para criar campanhas de posicionamento de marca premium

## Fluxo de Trabalho (Workflow)

Siga estes passos rigorosamente ao criar uma VSL com esta skill:

### Passo 1: Entendimento e Coleta de Dados

Antes de escrever qualquer linha de copy, você precisa entender o produto e o mercado.

1. **Pergunte ao usuário** as informações básicas (se não fornecidas):
   - Qual é o produto/oferta?
   - Quem é o cliente ideal (ICP)?
   - Qual é o idioma desejado (Português ou Inglês)?
2. **Execute o script de pesquisa** para gerar perguntas de aprofundamento:
   - Execute: `python scripts/vsl_research.py`
   - Use as perguntas geradas para entrevistar o usuário sobre detalhes específicos do ICP e os elementos necessários para cada fase do Kishōtenketsu.
3. **Faça pesquisa de mercado** usando a ferramenta `search` para entender o nicho, concorrentes e tendências atuais que podem ser usadas no roteiro.

### Passo 2: Estudo do Framework

Se você não estiver totalmente familiarizado com a estrutura Kishōtenketsu aplicada a vendas:

1. **Leia a referência obrigatória**:
   - Leia o arquivo `references/kishotenketsu_framework.md`
   - Preste atenção especial às diferenças entre as fases e aos "Red Flags" (erros comuns).

A estrutura é composta por 4 atos:
- **KI (Introdução, 0-15%)**: História emocional sem menção ao produto.
- **SHO (Desenvolvimento, 15-50%)**: Conexão da história com o problema do cliente. Sem linguagem de vendas.
- **TEN (Reviravolta, 50-85%)**: O clímax. A revelação inesperada que introduz o produto como solução óbvia.
- **KETSU (Conclusão, 85-100%)**: Reafirmação da oferta e Call-to-Action elegante.

### Passo 3: Geração do Roteiro e Storyboard

Após reunir todas as informações, gere os artefatos finais:

1. **Use os templates** para garantir a formatação correta:
   - Roteiro: `templates/vsl_script_template.md`
   - Storyboard: `templates/vsl_storyboard_template.md`
2. **Preencha os templates** com a copy persuasiva baseada na pesquisa e nas respostas do usuário.
3. **Gere o roteiro usando o script (opcional)** se precisar de uma base rápida para começar:
   - Edite o script `scripts/vsl_generator.py` com os dados do usuário na seção `example_data` e execute-o.

### Passo 4: Revisão e Entrega

1. Revise a copy gerada contra o "Quality Checklist" presente no arquivo de referência.
2. Certifique-se de que o produto **NÃO** é mencionado antes da fase TEN.
3. Salve os arquivos finais (Roteiro e Storyboard) em formato Markdown ou PDF.
4. Entregue ao usuário com uma explicação de como a estrutura Kishōtenketsu foi aplicada especificamente ao produto dele.

## Diretrizes de Copywriting

- **Elegância acima de agressividade**: O Kishōtenketsu vende pela força da revelação (Ten), não pela pressão. Evite gatilhos de escassez falsos ou linguagem desesperada.
- **O Teste da Mãe**: A copy deve ser tão honesta e o produto tão bom que o usuário venderia para a própria mãe.
- **Vestígios (Pistas)**: Plante pistas sutis na fase KI que só farão sentido quando a revelação acontecer na fase TEN.
- **Duração**: Mantenha o roteiro focado. A VSL ideal deve ter entre 3 e 5 minutos de duração lida em ritmo normal.
