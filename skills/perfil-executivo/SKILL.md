---
name: perfil-executivo
description: Cria ou atualiza Sumários Executivos / Perfis Executivos em PDF — capa, sumário navegável, seções numeradas, bloco de conversão e página de encerramento com marca. Use esta skill sempre que o usuário pedir para criar, gerar, atualizar ou reformular um "perfil executivo", "sumário executivo", "executive summary", "ebook de apresentação", "documento de posicionamento" ou qualquer documento de apresentação profissional de pessoa física ou empresa. Acione também quando o usuário enviar um PDF existente e pedir para atualizar ou modificar seu conteúdo. A renderização é delegada à skill horus-pdf-design; esta skill define a ESTRUTURA e a COPY do documento.
---

# Perfil Executivo

Documento de apresentação de uma pessoa ou empresa: quem é, o que faz, por que
importa, e qual o próximo passo. O que esta skill entrega é a **arquitetura de
conteúdo e a copy** — a parte visual é da `horus-pdf-design`.

## Divisão de responsabilidade

| Aqui | Na `horus-pdf-design` |
|---|---|
| Que seções existem e em que ordem | Capa, sumário, paginação, encerramento |
| O que cada seção precisa provar | Cor, tipografia, componentes, emblema |
| Tom, promessa, estrutura de argumento | Geração do PDF (Chrome headless) |

Antes, esta skill carregava o próprio pipeline WeasyPrint e uma paleta que não
existe mais no canon da marca (`#0d0a2e`, `#00c9b1`, `#7b4fff`). Isso saiu: a
identidade visual mora em um lugar só.

---

## Fluxo

### 1. Capturar o contexto

| Campo | Descrição |
|---|---|
| `nome_pessoa` | protagonista do perfil |
| `nome_empresa` | empresa / ecossistema |
| `tagline_empresa` | uma frase, sem adjetivo vago |
| `secoes` | lista de seções — ver §3 |
| `cta` | próximo passo concreto (opcional) |
| `produto` | qual marca assina o documento — ver §2 |

Se o usuário enviou um PDF para atualizar, extraia esses campos do conteúdo dele
antes de perguntar qualquer coisa.

### 2. Escolher a marca

Documento que a Horus assina usa o produto correspondente (`brand` é o default,
`estagiario`, `office`, `jurislab`, `advocacia`, `orchestrator`).

Perfil de **cliente**, com a identidade do cliente, usa `produto: "custom"` com
as `cores` dele e `emblema: False` — o vórtice é da Horus e não entra em
documento de terceiro. Detalhe na referência de produtos da `horus-pdf-design`.

### 3. Estrutura de páginas

```
1        CAPA           badge, nome, tagline, data
2        SUMÁRIO
3..N-2   SEÇÕES         uma ou mais páginas cada
N-1      CTA            opcional
N        ENCERRAMENTO   marca e assinatura
```

Seções padrão, quando o usuário não define — adapte ao nicho, não use como
formulário:

```
01  O ecossistema e a visão estratégica
02  O paradigma que mudou no mercado
03  Perfil pessoal: a mente por trás
04  Perfil empresarial
05  Como as ideias são geradas e validadas
06  Metodologia de decisão
07  Visão de mercado e posicionamento
08  O diferencial competitivo
09  Estratégia de expansão
10  Conclusão e convite
```

Guia de copy por seção: `references/conteudo_sections.md`.

### 4. Gerar

Monte o dict e chame a skill `horus-pdf-design`:

```python
generate_pdf({
    "titulo": "Sumário Executivo — {nome_pessoa}",
    "subtitulo": "{tagline_empresa}",
    "produto": "brand",
    "tipo_documento": "PERFIL EXECUTIVO",
    "secoes": [
        {"titulo": "O ecossistema e a visão estratégica",
         "intro": "Uma frase que estabelece a tese da seção.",
         "conteudo_html": "<div class='card'>…</div>"},
    ],
    "cta_final": {
        "kicker": "PRÓXIMO PASSO",
        "titulo": "…",
        "descricao": "…",
        "itens": ["…"],
        "acao": {"label": "Falar com a equipe", "url": "…"},
    },
    "marca_final": "{nome_empresa}",
    "tagline_final": "{tagline_empresa}",
})
```

Componentes disponíveis para `conteudo_html`: `.card`, `.card-dim`,
`.fluxo-passo`, `.lista-check`, `.destaque`, `.citacao`, `.metrica`, `.tabela` —
catálogo completo na referência de componentes da `horus-pdf-design`. Não
escreva CSS aqui.

### 5. Entregar

Informe o número de páginas e as seções incluídas. O caminho de saída sai no
retorno de `generate_pdf()`.

---

## Regras de copy

O que separa um perfil executivo de um panfleto:

- **Promessa com número concreto.** "3x em 6 meses" e não "muito mais". Se não
  há número, a afirmação é opinião — apresente como opinião.
- **Voz "você".** O leitor é o protagonista da decisão, não o cliente do texto.
- **Especialista que respeita o leitor**, não guru nem vendedor agressivo.
- **Sem urgência artificial.** Nada de contagem regressiva, "últimas vagas" ou
  "oferta por tempo limitado" quando não é verdade — e quando é, diga a data.
- **Sem emoji** em superfície de cliente. A seção é identificada pelo número e
  pelo traço de gradiente, que a `horus-pdf-design` já desenha.
- **Uma ideia por bloco.** Card que precisa de três parágrafos é três cards ou
  uma seção.

## Atualizar um perfil existente

1. Leia o PDF e extraia o conteúdo por seção.
2. Identifique o que muda — seção nova, dados, CTA.
3. Preserve a estrutura de argumento; não reescreva o que não foi pedido.
4. Regenere o documento inteiro (a paginação depende do conjunto).

Documento antigo pode vir na paleta aposentada. A `horus-pdf-design` avisa se
encontrar esses hex no `conteudo_html` — trate o aviso, não o ignore.

## Referências

- `references/conteudo_sections.md` — guia de copy por seção
- `references/html_templates.md` — para onde foram os templates
