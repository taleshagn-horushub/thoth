#!/usr/bin/env python3
"""
extract.py — Extrai texto limpo + estrutura de um documento longo (PDF ou Markdown/TXT)
para alimentar o doc-idea-miner.

Por que existe: minerar ideias de um documento denso começa por ter o texto em mãos,
limpo e com a estrutura preservada (headings/seções). Fazer isso à mão num PDF de 80
páginas é inviável e propenso a erro. Este script entrega texto normalizado + um índice
de seções candidatas, para o agente saber por onde navegar.

Uso:
    python scripts/extract.py <caminho-do-doc> [--out <arquivo-de-saida.txt>]

Saídas:
    - Escreve o texto limpo em --out (default: <doc>.extracted.txt ao lado do original)
    - Imprime no stdout um JSON com metadados: paginas, chars, words, headings[], out_path

Dependências: PDF usa `pypdf` (puro Python, sem libs nativas — seguro no Windows).
    Instale com:  py -m pip install pypdf      (ou: pip install pypdf)
    .md/.txt não precisam de dependência.

Nota de ambiente: NÃO depende de WeasyPrint/GTK. Aqui só LEMOS documentos; geração de
PDF no Windows é outro problema (ver memória do ecossistema).
"""

import argparse
import json
import os
import re
import sys

# No Windows o stdout default é cp1252 e quebra ao imprimir headings com acento/emoji.
# Forçar UTF-8 garante que o JSON de metadados saia íntegro em qualquer console.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass  # Python <3.7 ou stream sem reconfigure — segue sem forçar


def read_markdown(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def read_pdf(path: str) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.stderr.write(
            "ERRO: pypdf não instalado. Rode: py -m pip install pypdf\n"
        )
        sys.exit(2)

    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception as e:  # página corrompida não derruba o doc inteiro
            sys.stderr.write(f"aviso: falha ao extrair uma página: {e}\n")
            pages.append("")
    # \f (form feed) marca quebra de página — útil pro agente referenciar "pág. N"
    return "\f".join(pages)


def clean_text(text: str) -> str:
    # Une palavras quebradas por hífen no fim da linha: "respon-\nsabilidade" -> "responsabilidade"
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    # Colapsa 3+ quebras de linha em no máximo 2 (preserva parágrafos)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Remove espaços à direita
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip()


HEADING_PATTERNS = [
    re.compile(r"^#{1,6}\s+.+"),                       # Markdown headings
    re.compile(r"^\s*\d+(\.\d+)*[\.\)]?\s+\S.{0,80}$"),  # "1." / "2.3 Título"
    re.compile(r"^\s*(CAP[IÍ]TULO|SE[ÇC][ÃA]O|ART(?:IGO)?\.?|T[IÍ]TULO)\s+.+", re.IGNORECASE),
]


def detect_headings(text: str, limit: int = 80) -> list:
    """Heurística leve para listar seções candidatas — não é parser perfeito,
    é um índice navegável. Linhas curtas, numeradas, ALLCAPS ou Markdown viram heading."""
    headings = []
    for raw in text.split("\n"):
        line = raw.strip()
        if not line or len(line) > 100:
            continue
        is_heading = False
        for pat in HEADING_PATTERNS:
            if pat.match(line):
                is_heading = True
                break
        # ALLCAPS curto (provável título de seção)
        if not is_heading and line.isupper() and 3 <= len(line) <= 80:
            is_heading = True
        if is_heading:
            headings.append(line)
        if len(headings) >= limit:
            break
    return headings


def main():
    ap = argparse.ArgumentParser(description="Extrai texto limpo + estrutura de PDF/MD.")
    ap.add_argument("input", help="Caminho do documento (.pdf, .md, .markdown, .txt)")
    ap.add_argument("--out", help="Arquivo de saída do texto limpo")
    args = ap.parse_args()

    path = args.input
    if not os.path.isfile(path):
        sys.stderr.write(f"ERRO: arquivo não encontrado: {path}\n")
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        raw = read_pdf(path)
    elif ext in (".md", ".markdown", ".txt"):
        raw = read_markdown(path)
    else:
        sys.stderr.write(f"ERRO: extensão não suportada: {ext} (use .pdf, .md ou .txt)\n")
        sys.exit(1)

    text = clean_text(raw)
    pages = raw.count("\f") + 1 if "\f" in raw else 1
    words = len(text.split())
    headings = detect_headings(text)

    out_path = args.out or (os.path.splitext(path)[0] + ".extracted.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    meta = {
        "input": path,
        "out_path": out_path,
        "pages": pages,
        "chars": len(text),
        "words": words,
        "headings": headings,
        "long_doc": words > 8000,  # sinaliza p/ o agente fazer chunk + síntese
    }
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
