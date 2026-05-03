<div align="center">

# Thoth

**Skills your AI agents actually need.**

Production-tested agentic skills, prompts, and processes — born in real businesses, not in playgrounds.

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](./LICENSE)
[![Skills Format](https://img.shields.io/badge/format-Anthropic_Skills-blue.svg)](#skill-format)
[![Status](https://img.shields.io/badge/status-early_access-orange.svg)](#)

</div>

---

## What is Thoth?

Thoth is a curated, open-source library of **agentic skills** — bundles of system prompts, references, scripts, and templates that turn a generic AI agent into a domain specialist.

Every skill in this repo:

- ✅ Is **production-tested** in a real business workflow before landing here
- ✅ Follows the [Anthropic Skills format](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — drop-in compatible with Claude Code, the Agent SDK, and the Anthropic API
- ✅ Auto-converts to GitHub Copilot prompts/instructions and Cursor rules via the build pipeline
- ✅ Ships with usage examples, guardrails, and a clear definition of when *not* to invoke it

> Named after [Thoth](https://en.wikipedia.org/wiki/Thoth) — the Egyptian god of writing, knowledge, and magic. The skill library that pairs with the [Horus](https://horushub.com.br) ecosystem of AI-native legal operations.

---

## Why this exists

Generic LLMs are smart but unfocused. The same model that writes a legal contract one minute and a sales email the next will produce mediocre results on both unless you scaffold it with the right context, references, and constraints.

That scaffolding is a **skill** — and writing good ones is hard, slow, and expensive. Most teams reinvent the wheel for every new use case.

Thoth is the inverse: a curated library where every skill has already proven itself in production, with the prompts, examples, and guardrails that make it work.

**The mantra:** if it hasn't been used in a real business, it doesn't belong here.

---

## Quickstart

### Use a skill in Claude Code

```bash
git clone https://github.com/taleshagn-horushub/thoth.git
cp -r thoth/skills/horus-content-creator ~/.claude/skills/
```

The skill is now available in any Claude Code session.

### Use a skill via the Anthropic SDK

```ts
import Anthropic from "@anthropic-ai/sdk";
import { readFileSync } from "fs";

const skill = readFileSync("./thoth/skills/horus-content-creator/SKILL.md", "utf8");

const message = await new Anthropic().messages.create({
  model: "claude-opus-4-5",
  max_tokens: 4096,
  system: skill,
  messages: [{ role: "user", content: "Crie uma campanha Meta Ads para escritório trabalhista." }],
});
```

### Use as a git submodule (recommended for production)

If your runtime needs to read skills at execution time (e.g. an event-driven orchestrator), pin them as a submodule:

```bash
git submodule add https://github.com/taleshagn-horushub/thoth.git vendor/thoth
```

This is how the [horus-core](https://github.com/taleshagn-horushub/horus-core) orchestrator consumes Thoth skills in production.

---

## What's inside

```
thoth/
├── skills/                    # Anthropic Skills format (canonical source)
│   ├── horus-content-creator/        # Estratégia de marketing jurídico de alta conversão
│   └── market-research-offers-strategy/  # Wide research + Value Ladder
├── scripts/
│   └── build.ts                     # Generates Copilot/Cursor formats from canonical
├── docs/
│   ├── skill-format.md              # Authoring spec
│   └── contributing.md              # How skills get accepted
├── .github/workflows/
│   └── validate-skills.yml          # CI: lint frontmatter, broken refs, etc
├── LICENSE                          # MIT
└── README.md
```

### Skill format

Every skill is a folder with this layout:

```
my-skill/
├── SKILL.md           # Required. System prompt + frontmatter (name, description)
├── references/        # Optional. Markdown files the skill reads on demand
├── templates/         # Optional. Output templates (markdown, txt, html)
└── scripts/           # Optional. Helper scripts (Python, Node, etc)
```

The frontmatter follows the [Anthropic Skills spec](https://docs.claude.com/en/docs/agents-and-tools/agent-skills):

```yaml
---
name: my-skill
description: One paragraph that lets the model decide *when* to invoke this skill. Be specific.
---
```

See [`docs/skill-format.md`](./docs/skill-format.md) for the full authoring guide.

---

## Skills available

| Skill | Domain | What it does |
|---|---|---|
| [`horus-content-creator`](./skills/horus-content-creator/) | Marketing jurídico | Estratégia completa Meta Ads + Google Ads + Landing Page com compliance OAB |
| [`market-research-offers-strategy`](./skills/market-research-offers-strategy/) | Estratégia comercial | Wide Research de competidores + criação de Value Ladder produtizada |
| [`llm-council`](./skills/llm-council/) | Decision support | 5 AI advisors com lentes opostas + peer review anônimo + chairman synthesis. Adaptado da metodologia Karpathy |
| [`perfil-executivo`](./skills/perfil-executivo/) | Document generation | Gera Sumários / Perfis Executivos em PDF de alto impacto via WeasyPrint (HTML+CSS), com capa, sumário, encarte de oferta e branding |

> 🚧 More skills landing soon. See [the roadmap](#roadmap).

---

## Roadmap

The next batch of skills targets the 7 operational flows of an AI-first agency, including:

- `onboarding-strategist` — diagnóstico inicial de cliente novo
- `briefing-extractor` — extração estruturada de briefings em texto livre
- `calendar-scheduler` — agendamento via linguagem natural
- `message-composer` — comunicação cliente em pt-BR mercado jurídico
- `follow-up-watcher` — detecção de leads parados em pipeline
- `campaign-optimizer` — análise diária de campanhas + ajustes propostos
- `video-editor-brief` — geração de roteiro técnico para edição

If your business has a workflow that an AI specialist could own end-to-end, [open an issue](https://github.com/taleshagn-horushub/thoth/issues) — we want to hear it.

---

## Contributing

Quality > quantity. Every skill in `main` has earned its place by surviving real production use.

If you want to contribute a skill, the bar is:

1. **Used in production** for at least 30 days, by you or your team
2. **Self-contained** — frontmatter, references, and templates all present
3. **Guardrailed** — explicit rules for when *not* to invoke + how to refuse
4. **Tested** — at least 3 example prompts with expected behavior in the PR description

See [`docs/contributing.md`](./docs/contributing.md) for full guidelines.

---

## License

[MIT](./LICENSE) — use freely, fork freely, just don't strip attribution from contributed skills.

---

<div align="center">
Built and maintained by the team behind <a href="https://horushub.com.br">Horus</a>.
<br/>
<sub>Open-source skills. Production-tested. Born in real businesses.</sub>
</div>
