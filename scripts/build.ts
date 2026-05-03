// thoth/scripts/build.ts
//
// Converte os skills canônicos em ./skills/ pra formatos derivados:
//
//   1. GitHub Copilot — `.github/prompts/<slug>.prompt.md`
//      (frontmatter Copilot-nativo + body)
//
//   2. Plain system prompts — `dist/system-prompts/<slug>.txt`
//      (body sem frontmatter, pra uso direto via API Anthropic)
//
//   3. Catálogo JSON — `dist/catalog.json`
//      (índice consultável: name, description, path, version)
//
// Roda localmente: `npm run build`
// Roda em CI: pode publicar `dist/` como artifact ou GitHub Pages.

import { readdirSync, readFileSync, writeFileSync, mkdirSync, statSync, rmSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dirname ?? __dirname, "..");
const SKILLS_DIR = join(ROOT, "skills");
const COPILOT_DIR = join(ROOT, ".github", "prompts");
const SYSTEM_PROMPTS_DIR = join(ROOT, "dist", "system-prompts");
const CATALOG_PATH = join(ROOT, "dist", "catalog.json");

interface SkillFrontmatter {
  name: string;
  description: string;
  version?: string;
  license?: string;
  tags?: string[];
}

interface ParsedSkill {
  slug: string;
  frontmatter: SkillFrontmatter;
  body: string;
}

function parseSkill(slug: string): ParsedSkill | null {
  const skillMd = join(SKILLS_DIR, slug, "SKILL.md");
  let raw: string;
  try {
    raw = readFileSync(skillMd, "utf8");
  } catch {
    return null;
  }

  const fmMatch = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!fmMatch) return null;

  const fmRaw = fmMatch[1];
  const body = fmMatch[2].trim();

  // Parser YAML mínimo — frontmatter de skill é flat (sem aninhamento profundo)
  const fm: Record<string, string> = {};
  for (const line of fmRaw.split("\n")) {
    const m = line.match(/^([a-zA-Z_]+):\s*(.+)$/);
    if (m) fm[m[1]] = m[2].replace(/^["']|["']$/g, "").trim();
  }

  if (!fm.name || !fm.description) return null;

  return {
    slug,
    frontmatter: fm as unknown as SkillFrontmatter,
    body,
  };
}

function listSkills(): ParsedSkill[] {
  const entries = readdirSync(SKILLS_DIR);
  const skills: ParsedSkill[] = [];
  for (const slug of entries) {
    if (!statSync(join(SKILLS_DIR, slug)).isDirectory()) continue;
    const parsed = parseSkill(slug);
    if (parsed) skills.push(parsed);
  }
  return skills;
}

function buildCopilotFormat(skill: ParsedSkill): string {
  // Copilot prompts (.github/prompts/*.prompt.md):
  // https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
  const fm = [
    "---",
    `mode: 'agent'`,
    `description: ${JSON.stringify(skill.frontmatter.description)}`,
    "---",
    "",
  ].join("\n");
  return fm + skill.body + "\n";
}

function buildSystemPrompt(skill: ParsedSkill): string {
  // Plain text — apenas o body. Frontmatter já é metadata, não vai pro prompt.
  return skill.body + "\n";
}

function ensureCleanDir(path: string) {
  try {
    rmSync(path, { recursive: true, force: true });
  } catch {}
  mkdirSync(path, { recursive: true });
}

function main() {
  const skills = listSkills();
  if (skills.length === 0) {
    console.error("Nenhuma skill encontrada em skills/");
    process.exit(1);
  }

  ensureCleanDir(COPILOT_DIR);
  ensureCleanDir(SYSTEM_PROMPTS_DIR);

  const catalog: Array<{
    name: string;
    slug: string;
    description: string;
    version?: string;
    path: string;
  }> = [];

  for (const skill of skills) {
    // Copilot format
    writeFileSync(
      join(COPILOT_DIR, `${skill.slug}.prompt.md`),
      buildCopilotFormat(skill),
      "utf8",
    );

    // Plain system prompt
    writeFileSync(
      join(SYSTEM_PROMPTS_DIR, `${skill.slug}.txt`),
      buildSystemPrompt(skill),
      "utf8",
    );

    catalog.push({
      name: skill.frontmatter.name,
      slug: skill.slug,
      description: skill.frontmatter.description,
      version: skill.frontmatter.version,
      path: `skills/${skill.slug}/`,
    });

    console.log(`✓ ${skill.slug}`);
  }

  writeFileSync(
    CATALOG_PATH,
    JSON.stringify({ generated_at: new Date().toISOString(), skills: catalog }, null, 2),
    "utf8",
  );

  console.log(`\n${skills.length} skills built → .github/prompts/, dist/system-prompts/, dist/catalog.json`);
}

main();
