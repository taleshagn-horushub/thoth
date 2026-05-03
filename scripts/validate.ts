// thoth/scripts/validate.ts
//
// Valida que todas as skills em ./skills/ seguem o formato canônico:
//   1. Cada skill é um diretório
//   2. Cada diretório tem um SKILL.md
//   3. Cada SKILL.md tem frontmatter com `name` e `description`
//   4. O `name` no frontmatter bate com o nome do diretório
//   5. Toda referência a `references/`, `templates/`, `scripts/` aponta pra arquivo existente
//   6. Não há paths absolutos (/home/, C:\, /Users/)
//
// Roda em CI (.github/workflows/validate-skills.yml).
// Localmente: `npx tsx scripts/validate.ts`

import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

const SKILLS_DIR = resolve(import.meta.dirname ?? __dirname, "..", "skills");

type Issue = { skill: string; severity: "error" | "warning"; message: string };
const issues: Issue[] = [];

function err(skill: string, message: string) {
  issues.push({ skill, severity: "error", message });
}

function warn(skill: string, message: string) {
  issues.push({ skill, severity: "warning", message });
}

function parseFrontmatter(content: string): { name?: string; description?: string } | null {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;

  const raw = match[1];
  const out: Record<string, string> = {};
  for (const line of raw.split("\n")) {
    const m = line.match(/^([a-zA-Z_]+):\s*(.+)$/);
    if (m) out[m[1]] = m[2].replace(/^["']|["']$/g, "").trim();
  }
  return out;
}

function validateSkill(slug: string) {
  const dir = join(SKILLS_DIR, slug);
  const skillMd = join(dir, "SKILL.md");

  let content: string;
  try {
    content = readFileSync(skillMd, "utf8");
  } catch {
    err(slug, "SKILL.md ausente");
    return;
  }

  // Frontmatter
  const fm = parseFrontmatter(content);
  if (!fm) {
    err(slug, "SKILL.md sem frontmatter YAML");
    return;
  }
  if (!fm.name) err(slug, "frontmatter sem campo `name`");
  if (!fm.description) err(slug, "frontmatter sem campo `description`");
  if (fm.name && fm.name !== slug) {
    err(slug, `frontmatter.name (${fm.name}) não bate com diretório (${slug})`);
  }

  // Paths absolutos proibidos
  const absolutePathPattern = /(\/home\/|C:\\Users\\|\/Users\/[A-Za-z]+\/)/;
  if (absolutePathPattern.test(content)) {
    err(slug, "SKILL.md contém path absoluto — use caminhos relativos");
  }

  // Referências a arquivos
  const refs = [
    ...content.matchAll(/`(references\/[^\s`]+)`/g),
    ...content.matchAll(/`(templates\/[^\s`]+)`/g),
    ...content.matchAll(/`(scripts\/[^\s`]+)`/g),
  ];
  for (const m of refs) {
    const relPath = m[1];
    const fullPath = join(dir, relPath);
    try {
      statSync(fullPath);
    } catch {
      warn(slug, `referência aponta pra arquivo inexistente: ${relPath}`);
    }
  }
}

function main() {
  let entries: string[];
  try {
    entries = readdirSync(SKILLS_DIR);
  } catch {
    console.error(`Diretório skills/ não encontrado em ${SKILLS_DIR}`);
    process.exit(1);
  }

  const skills = entries.filter((e) => {
    try {
      return statSync(join(SKILLS_DIR, e)).isDirectory();
    } catch {
      return false;
    }
  });

  if (skills.length === 0) {
    console.warn("Nenhuma skill encontrada em skills/");
    return;
  }

  console.log(`Validando ${skills.length} skill(s)...\n`);
  for (const slug of skills) validateSkill(slug);

  const errors = issues.filter((i) => i.severity === "error");
  const warnings = issues.filter((i) => i.severity === "warning");

  for (const i of issues) {
    const icon = i.severity === "error" ? "❌" : "⚠️ ";
    console.log(`${icon} [${i.skill}] ${i.message}`);
  }

  console.log(`\n${skills.length} skills · ${errors.length} erros · ${warnings.length} avisos`);

  if (errors.length > 0) process.exit(1);
}

main();
