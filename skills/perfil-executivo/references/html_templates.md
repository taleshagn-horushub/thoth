# Templates HTML — movidos

Este arquivo continha 336 linhas de HTML e CSS com a paleta v1 da marca
(`#0d0a2e`, `#00c9b1`, `#7b4fff`, `#ffd700`) — capa, sumário, páginas de
conteúdo, encarte de oferta e encerramento, cada um com o próprio bloco de
`<style>`.

Nada disso vive mais aqui. Manter uma cópia do design system dentro de uma skill
de conteúdo foi exatamente o que fez a paleta aposentada continuar circulando
pelo ecossistema depois de trocada.

## Onde está agora

| O que você procura | Onde |
|---|---|
| Capa, sumário, paginação, encerramento | montados por `generate_pdf()` a partir do config |
| Componentes de conteúdo | `references/componentes.md` da `horus-pdf-design` |
| Cores, tipografia, contraste | `references/paleta.md` da mesma skill |
| Qual marca assina o documento | `references/produtos.md` |
| Encarte de oferta | virou `cta_final` no config |

## O encarte de oferta

Era um bloco com copy fixa: `✦ OFERTA EXCLUSIVA ✦`, desconto em dourado
(`#ffd700`), QR Code e `⏰ OFERTA POR TEMPO LIMITADO`.

Virou parâmetro, com defaults neutros:

```python
"cta_final": {
    "kicker": "PRÓXIMO PASSO",
    "titulo": "...",
    "descricao": "...",
    "itens": ["...", "..."],
    "preco": {"de": "...", "por": "...", "condicao": "..."},   # opcional
    "acao": {"label": "...", "url": "..."},
    "observacao": "...",                                        # opcional
}
```

Sem `preco`, o bloco vira um próximo passo institucional em vez de uma venda.

**O que se perdeu:** o placeholder de QR Code. O `.cta` do canon tem `acao.url`
mas não renderiza QR. Se voltar a ser necessário, o lugar de resolver é a
`horus-pdf-design`, não aqui.

**O que mudou de propósito:** a escassez deixou de ser obrigatória. O brand book
proíbe urgência artificial e emoji em superfície de cliente — os três elementos
fixos do encarte antigo violavam isso.
