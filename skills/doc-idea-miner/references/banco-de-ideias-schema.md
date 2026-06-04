# Schema do Banco de Ideias

O banco de ideias é a **interface estável** entre o `doc-idea-miner` (produtor) e o `multicanal-formatter` (consumidor). Por ser contrato entre dois estágios, os nomes dos campos importam: mantenha-os exatamente como abaixo para que o formatter saiba ler.

O formato canônico é Markdown (legível pelo humano e pelo agente). Há também uma forma JSON opcional, útil se o orquestrador for processar programaticamente.

## Campos de cada ideia

| Campo | Obrigatório | O que é |
|-------|-------------|---------|
| `id` | sim | Número sequencial (1, 2, 3…) para referência |
| `nucleo` | sim | A ideia central em **uma frase** memorável |
| `angulo` | sim | A perspectiva específica que torna esta ideia distinta de outras sobre o mesmo fato |
| `tensao` | sim | O conflito, surpresa ou problema que prende atenção |
| `insight` | sim | A verdade não-óbvia que o público leva ao consumir |
| `ancora` | sim | Citação/número/trecho **literal do documento** + referência (pág./seção). Se ausente: `[não encontrada — hipótese do agente]` |
| `publico` | sim | Para quem fala (ex.: advogado tributarista, dono de PME, leigo com dúvida sobre direito X) |
| `canal_sugerido` | sim | Canal mais forte (`instagram` / `linkedin` / `tiktok` / `youtube`) + 1 linha de porquê |
| `gatilho` | recomendado | Qual dos 8 gatilhos originou a ideia (ver extraction-heuristics.md) |
| `serie` | opcional | Eixo temático ao qual pertence (preenchido na consolidação) |

## Forma Markdown (canônica)

```markdown
### Ideia 1 — <título curto>

- **Núcleo:** <uma frase>
- **Ângulo:** <perspectiva>
- **Tensão:** <conflito/surpresa>
- **Insight:** <verdade não-óbvia>
- **Âncora:** "<trecho literal>" (pág. X / seção Y)
- **Público:** <quem>
- **Canal sugerido:** <canal> — <porquê em 1 linha>
- **Gatilho:** <nome do gatilho>
```

## Forma JSON (opcional)

```json
{
  "documento_fonte": "voto-stj-resp-123.pdf",
  "data": "2026-06-04",
  "ideias": [
    {
      "id": 1,
      "nucleo": "...",
      "angulo": "...",
      "tensao": "...",
      "insight": "...",
      "ancora": { "trecho": "...", "ref": "pág. 12" },
      "publico": "...",
      "canal_sugerido": { "canal": "linkedin", "porque": "..." },
      "gatilho": "afirmacao-contraintuitiva",
      "serie": "Prazos que pegam todo mundo"
    }
  ],
  "maquina_de_ideias": [
    { "eixo": "Prazos que pegam todo mundo", "ideias": [1, 4, 7] }
  ]
}
```

## Seção "Máquina de Ideias"

Depois de listar as ideias, agrupe-as em **3–5 eixos temáticos**. Isso transforma uma lista solta num plano de série: o usuário vê que as ideias 1, 4 e 7 contam uma história maior sobre "prazos", e pode planejar uma semana de conteúdo em vez de um post avulso. Cada eixo: um nome + os `id`s das ideias que o compõem.
