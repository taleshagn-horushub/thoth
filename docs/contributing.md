# Contributing to Thoth

Thoth is curated. The bar to merge is high — not because we want to gatekeep, but because every skill on `main` carries the implicit promise that it works in production.

## The bar

A skill is mergeable when:

1. **Used in production for ≥30 days** by the contributor or their team. Side-project demos don't count.
2. **Self-contained** — `SKILL.md` with valid frontmatter, plus any `references/` / `templates/` / `scripts/` it points to.
3. **Guardrailed** — explicit `## Guardrails` section per [`skill-format.md`](./skill-format.md).
4. **Documented** — at least 3 example prompts in the PR description showing expected behavior + 1 example showing graceful refusal.
5. **Format-compliant** — passes `npm run validate` (CI will run this for you).

If your skill doesn't clear the bar, that's fine — open an issue first to discuss the path. Maintainers will help shape it.

## The PR checklist

Copy this into your pull request description:

```markdown
### Skill: `<slug>`

**Production track record:** <where it's been used, for how long, what outputs it has produced>

**Domain & target user:** <who is this for>

**Sample prompts**

1. *Happy path:* `<prompt>` → expected output sketch
2. *Edge case:* `<prompt>` → how the skill handles it
3. *Refusal:* `<prompt that should be refused>` → expected refusal pattern

**References / templates / scripts changed:**

- [ ] All paths in `SKILL.md` are relative (no `/home/...` or `C:\...`)
- [ ] No PII or proprietary client data in references
- [ ] All external links resolve
- [ ] Scripts are non-destructive by default
```

## Naming

Skills are named in **kebab-case** with a verb-noun or domain-action shape:

- ✅ `briefing-extractor`, `campaign-optimizer`, `calendar-scheduler`
- ❌ `helper`, `marketing`, `the-one-skill-to-rule-them-all`

If unsure, propose 2–3 candidates in the PR description.

## What we won't merge

- Skills that wrap a single LLM call without scaffolding (just use the API directly)
- Skills containing client-identifiable data
- Skills that promise specific business outcomes ("guarantees 3x leads")
- Skills built around a specific paid tool unless it's industry-standard
- Skills that duplicate an existing one without a clear differentiation

## Maintainers

Currently maintained by the team behind [Horus](https://horushub.com.br). The maintainer list will grow as contributors land 2+ accepted skills.

## License

By contributing, you agree your skill is released under the [MIT license](../LICENSE). You retain authorship credit via the optional `authors` field in frontmatter.
