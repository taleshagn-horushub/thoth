# Skill Format

Every skill in Thoth follows the [Anthropic Skills format](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) — a folder containing a required `SKILL.md` plus optional `references/`, `templates/`, and `scripts/` subdirectories.

This page is the canonical authoring spec. If you're contributing a skill, read this end-to-end first.

---

## Folder layout

```
skills/<slug>/
├── SKILL.md              # required
├── references/           # optional — files the skill reads on demand
│   └── *.md
├── templates/            # optional — output skeletons
│   └── *.{md,txt,html}
└── scripts/              # optional — helper scripts
    └── *.{py,ts,sh}
```

The `<slug>` must be **kebab-case**, descriptive, and unique within the repo:

- ✅ `horus-content-creator`, `briefing-extractor`, `calendar-scheduler`
- ❌ `Skill1`, `marketing_helper`, `the-best-skill-ever`

---

## SKILL.md anatomy

### Required: frontmatter

The first thing in `SKILL.md` is YAML frontmatter with two required fields:

```yaml
---
name: my-skill
description: One paragraph (1-3 sentences) that lets the model decide *when* to invoke this skill. Mention concrete use cases, the domain, and the type of output. Avoid generic adjectives ("powerful", "amazing"). Be specific.
---
```

Optional fields:

```yaml
---
name: my-skill
description: ...
license: MIT
version: 1.0.0
tags: [marketing, legal, copywriting]
authors:
  - name: Tales Hagn
    url: https://horushub.com.br
---
```

> 💡 **Why `description` matters more than you think.** When multiple skills are available, the model reads only the descriptions to decide which to invoke. A vague description means your skill never gets picked. Write it like a search snippet: clear use case, clear output type.

### Body

After the frontmatter, the body is the system prompt the agent will receive. Structure it with these sections (in order):

1. **`# <Skill Title>`** — H1 with the human-friendly title
2. **`## Visão Geral` / Overview** — what the skill does, who it serves, and what it produces
3. **`## Entradas Obrigatórias` / Required Inputs** — the briefing fields the agent should validate before producing output
4. **`## Fluxo Operacional` / Operational Flow** — the step-by-step process, often broken into phases
5. **`## Padrões de Saída` / Output Patterns** — what the deliverables look like
6. **`## Guardrails`** — explicit rules. When to refuse, when to ask, what never to do
7. **`## Recursos e Referências` / Resources** — pointers to the `references/`, `templates/`, `scripts/` files

Bilingual is fine (pt-BR + English). Match the language of your target users.

---

## References

Use `references/` for content that's too long to live inline in `SKILL.md` but that the agent should read when the situation demands it.

Examples:

- Brand books, style guides
- Domain glossaries (legal terms, industry jargon)
- Frameworks (AIDA, PAS, JTBD, etc)
- Compliance rules (OAB, GDPR, LGPD)

In `SKILL.md`, reference them with **relative paths**:

```markdown
For brand voice, read `references/brand_e_compliance.md`.
```

> ⚠️ **Never use absolute paths** like `/home/ubuntu/...` or `C:\Users\...`. Skills are designed to be portable.

---

## Templates

Use `templates/` for output skeletons the agent can fill in. Common formats:

- `*.md` — internal docs, blog posts, SOPs
- `*.html` — landing pages, decks
- `*.txt` — email drafts, message templates

Reference them the same way:

```markdown
Use `templates/landing_page.html` as the structural skeleton.
```

---

## Scripts

Use `scripts/` for executable helpers:

- Validation (e.g. `validate_strategy.py`)
- Integration with external APIs (e.g. `create_todoist_tasks.py`)
- Data transformation

Scripts must:

- Be self-contained (declare dependencies inline or via `requirements.txt`)
- Print clear errors on failure
- Never make destructive calls (delete, drop, etc) without an explicit `--confirm` flag

---

## Guardrails — non-negotiable

Every skill must have a `## Guardrails` section. At minimum, address:

1. **What to do when input is incomplete** — ask, or assume + flag?
2. **What types of requests to refuse** — out of scope, unethical, hallucination-prone?
3. **What never to invent** — laws, statistics, named cases, prices, contact info?
4. **How to handle conflicts** with brand or compliance rules?

Skills without guardrails will not be merged.

---

## Versioning

Skills are versioned with semver in the optional `version` frontmatter field:

- **Patch** (1.0.0 → 1.0.1) — typo fixes, clarifications, no behavior change
- **Minor** (1.0.0 → 1.1.0) — new sections, additional references, expanded scope (backward-compatible)
- **Major** (1.0.0 → 2.0.0) — behavior change, removed sections, renamed deliverables

Bump the version on every meaningful PR. The CI will check this.

---

## Build pipeline

Canonical skills live in `skills/`. The build script (`scripts/build.ts`) generates derivative formats:

- **GitHub Copilot** — `.github/prompts/<slug>.prompt.md` + `.github/instructions/<slug>.instructions.md`
- **Cursor Rules** — `.cursorrules` files (if applicable)
- **Plain system prompts** — `dist/system-prompts/<slug>.txt` for direct API use

You don't author derivative formats by hand. Edit the canonical `SKILL.md` and run `npm run build`.
