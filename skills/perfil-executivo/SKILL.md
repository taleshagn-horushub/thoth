---
name: perfil-executivo
description: Cria ou atualiza Sumários Executivos / Perfis Executivos completos em PDF, no estilo do documento Horus/CSI Jurídico — capa com gradiente escuro, sumário navegável, seções numeradas com emojis, cards de conteúdo, encarte de oferta e página de encerramento com marca. Use esta skill sempre que o usuário pedir para criar, gerar, atualizar ou reformular um "perfil executivo", "sumário executivo", "executive summary", "ebook de apresentação", "documento de posicionamento" ou qualquer documento de apresentação profissional de pessoa física ou empresa. Acione também quando o usuário enviar um PDF existente e pedir para atualizar ou modificar seu conteúdo.
---

# Perfil Executivo — Skill

Skill para criar e atualizar **Sumários / Perfis Executivos** em formato PDF visual de alto impacto, seguindo a estrutura e estética do documento de referência (Horus Hub / CSI Jurídico).

---

## Fluxo de Trabalho

### 1. Captura de Contexto

Antes de começar, colete (a partir do PDF enviado, da conversa ou perguntando ao usuário):

| Campo | Descrição |
|---|---|
| `nome_pessoa` | Nome do protagonista do perfil |
| `nome_empresa` | Nome da empresa / ecossistema |
| `tagline_empresa` | Slogan ou subtítulo da empresa |
| `data_documento` | Data de publicação (padrão: hoje) |
| `secoes` | Lista de seções com título, emoji e conteúdo |
| `oferta` | Dados do encarte de oferta (título, desconto, CTA, produto) |
| `cor_primaria` | Cor principal (padrão: `#1a1060` → roxo escuro) |
| `cor_acento` | Cor de acento (padrão: `#00c9b1` → ciano) |
| `logo_descricao` | Ícone/logotipo da capa (se não houver, usar ícone de camadas) |

Se o usuário enviou um PDF, extraia os campos acima diretamente do conteúdo. Para campos ausentes, use padrões ou pergunte de forma objetiva.

---

### 2. Estrutura Obrigatória do Documento

O PDF deve seguir **esta sequência de páginas**:

```
Página 1  — CAPA
Página 2  — SUMÁRIO
Página 3+ — SEÇÕES DE CONTEÚDO (uma seção por página, podendo ter múltiplas)
Penúltima — ENCARTE DE OFERTA
Última    — PÁGINA DE ENCERRAMENTO / MARCA
```

#### Página 1 — Capa
- Fundo: gradiente roxo/azul escuro com mancha roxa nos cantos
- Ícone centralizado (logotipo da empresa ou ícone padrão)
- Badge `EBOOK` acima do título
- Título grande em branco bold: `{nome_pessoa}` ou `Sumário Executivo {nome_pessoa}`
- Linha divisória colorida (gradiente roxo→ciano)
- Data em cinza claro
- Rodapé: nome da empresa em letras espaçadas maiúsculas

#### Página 2 — Sumário
- Título `Sumário` em branco
- Lista numerada com número em destaque colorido (gradiente), título da seção, linha pontilhada e número de página
- Fundo escuro consistente com capa

#### Páginas de Conteúdo
Cada seção segue o padrão:
- Número da seção + emoji + título em destaque
- Subtítulo/descrição introdutória
- Blocos de conteúdo: texto corrido, listas com ícones de check (`✓`), ou sub-blocos com título em ciano
- Rodapé com número de página e nome da empresa

#### Encarte de Oferta
- Badge `✦ OFERTA EXCLUSIVA ✦`
- Título da oferta em branco bold
- Descrição do produto
- Botão de CTA (cor de acento)
- Destaque de desconto + bônus
- Espaço para QR Code (placeholder se não fornecido)
- Rodapé de urgência

#### Página de Encerramento
- Ícone centralizado
- `PRODUZIDO COM` em letras espaçadas
- Nome da empresa em destaque com cores da marca
- Tagline/subtítulo em cinza

---

### 3. Seções Padrão (se não especificadas)

Se o usuário não definir as seções, use esta estrutura como ponto de partida e adapte ao nicho:

```
01 — O Ecossistema {empresa} e a Visão Estratégica de {nome}
02 — Introdução: O Novo Paradigma do Mercado
03 👤 Perfil Pessoal: A Mente por Trás da Inovação
04 🏢 Perfil Empresarial: {empresa}
05 💡 Processo de Geração e Validação de Ideias
06 ⚖️ Metodologia de Tomada de Decisão
07 🎯 Visão de Mercado e Posicionamento
08 🚀 O Diferencial Competitivo Único
09 📈 Estratégia de Expansão e Futuro
10 📝 Conclusão: O Convite à Transformação
```

---

### 4. Implementação Técnica

Use **Python com WeasyPrint** para gerar o PDF a partir de HTML+CSS.

#### Setup
```bash
pip install weasyprint --break-system-packages
```

#### Paleta de Cores (variáveis CSS)
```css
--bg-dark:     #0d0a2e;   /* fundo principal */
--bg-mid:      #1a1060;   /* fundo secundário */
--bg-card:     rgba(255,255,255,0.05); /* cards */
--accent-cyan: #00c9b1;   /* ciano */
--accent-purple: #7b4fff; /* roxo */
--text-white:  #ffffff;
--text-gray:   #a0a0c0;
--gradient-line: linear-gradient(90deg, #7b4fff, #00c9b1);
--gradient-btn:  linear-gradient(135deg, #7b4fff, #00c9b1);
```

#### Script base — `generate_profile.py`
```python
from weasyprint import HTML, CSS
import os

def generate_executive_profile(html_content: str, output_path: str):
    """Gera PDF a partir do HTML do perfil executivo."""
    css = CSS(string="""
        @page {
            size: A4;
            margin: 0;
        }
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #0d0a2e;
            color: #ffffff;
        }
        .page {
            width: 210mm;
            min-height: 297mm;
            page-break-after: always;
            position: relative;
            overflow: hidden;
        }
    """)
    HTML(string=html_content).write_pdf(output_path, stylesheets=[css])
    print(f"PDF gerado: {output_path}")
```

#### Estrutura HTML por Página

Veja `references/html_templates.md` para os templates HTML completos de cada tipo de página.

---

### 5. Regras de Estilo

- **Tipografia**: Títulos grandes (36–48px), corpo (13–14px), espaçamento generoso
- **Emojis nas seções**: Sempre usar em títulos de seção de conteúdo
- **Números de seção**: Exibir com fonte grande (48–64px) em baixa opacidade como elemento decorativo de fundo
- **Cards de conteúdo**: `background: rgba(255,255,255,0.05)`, `border-radius: 12px`, `border: 1px solid rgba(255,255,255,0.1)`
- **Listas**: Usar `✓` em ciano como marcador, ou bullets personalizados
- **Gradiente da linha divisória**: Sempre `linear-gradient(90deg, #7b4fff, #00c9b1)`, altura 3px
- **Botão CTA**: Gradiente roxo→ciano, `border-radius: 8px`, texto maiúsculo espaçado

---

### 6. Atualização de Perfil Existente

Se o usuário enviou um PDF para **atualizar**:

1. Leia o PDF e extraia todo o conteúdo por seção
2. Identifique o que o usuário quer mudar (nova seção, dados atualizados, nova oferta etc.)
3. Mantenha o estilo e estrutura originais
4. Regenere apenas as páginas afetadas e reconstrua o PDF completo
5. Entregue o PDF atualizado com `present_files`

---

### 7. Entrega

1. Gere o PDF em um caminho de output configurável (default: `./output/{nome_empresa}_perfil_executivo.pdf` ou o que o agente runtime expor)
2. Disponibilize o arquivo ao usuário pelo mecanismo de entrega do ambiente (Claude Code: link relativo no chat; Agent SDK: retornar path no resultado; sandbox tipo Manus: `present_files`)
3. Informe o número de páginas e as seções incluídas no resumo final

---

## Referências

- `references/html_templates.md` — Templates HTML de cada tipo de página
- `references/conteudo_sections.md` — Guia de copywriting para cada seção padrão
