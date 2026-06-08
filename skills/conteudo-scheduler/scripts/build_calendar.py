#!/usr/bin/env python3
"""
build_calendar.py — Distribui as peças de conteúdo num calendário com cadência por
canal e exporta em 3 formatos: calendar.csv (importável em qualquer agendador),
calendar.md (legível) e postiz-ready.json (payload pronto para o Postiz quando
houver integração).

Por que um script: matemática de datas (próxima terça às 9h, pular fim de semana,
distribuir N peças sem colisão) é exatamente o tipo de coisa que um LLM erra. O
script faz isso de forma determinística; o agente cuida do conteúdo.

Uso:
    python build_calendar.py pieces.json --start 2026-06-09 --out <pasta>
    python build_calendar.py pieces.json --start 2026-06-09 --cadence cadence.json --out <pasta>

pieces.json (entrada) — lista de peças a agendar:
    [
      {"channel": "linkedin", "title": "...", "asset": "linkedin/drafts.md", "caption": "linkedin/drafts.md"},
      {"channel": "instagram", "title": "...", "asset": "instagram/arte-ideia-02/", "caption": "instagram/drafts.md"}
    ]
    (channel ∈ instagram | linkedin | tiktok | youtube; asset/caption são caminhos relativos opcionais)

cadence.json (opcional) — sobrescreve a cadência default. Formato:
    { "linkedin": {"weekdays": [1,3], "time": "09:00"}, ... }
    weekday: 0=segunda ... 6=domingo.
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# Cadência default por canal (padrão Horus: Instagram é o feed diário; demais apoiam).
# weekday: 0=segunda ... 6=domingo. time em HH:MM (hora local).
DEFAULT_CADENCE = {
    "instagram": {"weekdays": [0, 1, 2, 3, 4, 5], "time": "18:00"},  # 1 post/dia útil (seg–sáb)
    "linkedin":  {"weekdays": [1, 3],             "time": "09:00"},  # ter/qui manhã
    "tiktok":    {"weekdays": [0, 2, 4],          "time": "12:00"},  # seg/qua/sex meio-dia
    "youtube":   {"weekdays": [2],                "time": "19:00"},  # qua à noite (semanal)
}

# Rodízio de pilares de conteúdo (guia editorial — não afeta a alocação de datas).
# Espelha a estratégia Horus (Educar 40 / Demonstrar 25 / Processo 20 / Autoridade 15).
PILAR_POR_DIA = {
    0: "Educar", 1: "Demonstrar", 2: "Processo", 3: "Autoridade", 4: "Oferta", 5: "Educar",
}

WEEKDAY_PT = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def next_slot(after: datetime, weekdays, hour, minute) -> datetime:
    """Primeiro horário >= `after` que cai num dos weekdays, no horário dado."""
    d = after
    for _ in range(0, 14):  # busca dentro de 2 semanas (cadência sempre cabe)
        if d.weekday() in weekdays:
            cand = d.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if cand >= after:
                return cand
        d = (d + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    # fallback: mesmo dia/hora (não deveria acontecer)
    return after.replace(hour=hour, minute=minute, second=0, microsecond=0)


def schedule(pieces, start: datetime, cadence):
    # Cursor por canal — cada canal avança independentemente nos seus dias.
    cursor = {ch: start for ch in cadence}
    scheduled = []
    for p in pieces:
        ch = p.get("channel", "").lower()
        cad = cadence.get(ch)
        if not cad:
            sys.stderr.write(f"aviso: canal sem cadência, pulando: {ch}\n")
            continue
        hh, mm = [int(x) for x in cad["time"].split(":")]
        slot = next_slot(cursor[ch], cad["weekdays"], hh, mm)
        scheduled.append({**p, "channel": ch, "datetime": slot})
        # próximo cursor desse canal: dia seguinte ao slot (pega o próximo weekday válido)
        cursor[ch] = slot + timedelta(days=1)
    scheduled.sort(key=lambda x: x["datetime"])
    return scheduled


def write_csv(rows, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["data", "hora", "dia", "canal", "titulo", "arte", "legenda", "status"])
        for r in rows:
            dt = r["datetime"]
            w.writerow([
                dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M"), WEEKDAY_PT[dt.weekday()],
                r["channel"], r.get("title", ""), r.get("asset", ""),
                r.get("caption", ""), "agendado",
            ])


def write_md(rows, path):
    lines = ["# Calendário de Conteúdo\n"]
    current_week = None
    for r in rows:
        dt = r["datetime"]
        wk = dt.isocalendar()[1]
        if wk != current_week:
            current_week = wk
            lines.append(f"\n## Semana {wk}\n")
        lines.append(
            f"- **{dt.strftime('%d/%m')} ({WEEKDAY_PT[dt.weekday()]}) {dt.strftime('%H:%M')}** "
            f"· `{r['channel']}` · _{PILAR_POR_DIA.get(dt.weekday(), '-')}_ — {r.get('title','(sem título)')}"
        )
        if r.get("asset"):
            lines.append(f"    - arte: `{r['asset']}`")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_postiz(rows, path):
    """Payload neutro, próximo do modelo do Postiz. Quando a integração existir,
    é só mapear cada item para a API. Por enquanto, é o export estruturado."""
    out = []
    for r in rows:
        out.append({
            "channel": r["channel"],
            "publishAt": r["datetime"].isoformat(),
            "title": r.get("title", ""),
            "assetPath": r.get("asset", ""),
            "captionPath": r.get("caption", ""),
            "status": "scheduled",
        })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)


def main():
    ap = argparse.ArgumentParser(description="Monta calendário de conteúdo e exporta CSV/MD/JSON.")
    ap.add_argument("pieces", help="JSON com a lista de peças a agendar")
    ap.add_argument("--start", required=True, help="Data de início AAAA-MM-DD")
    ap.add_argument("--cadence", help="JSON de cadência custom (sobrescreve o default)")
    ap.add_argument("--out", default=".", help="Pasta de saída dos exports")
    args = ap.parse_args()

    with open(args.pieces, encoding="utf-8") as f:
        pieces = json.load(f)

    cadence = dict(DEFAULT_CADENCE)
    if args.cadence:
        with open(args.cadence, encoding="utf-8") as f:
            cadence.update(json.load(f))

    start = datetime.strptime(args.start, "%Y-%m-%d")
    rows = schedule(pieces, start, cadence)

    os.makedirs(args.out, exist_ok=True)
    write_csv(rows, os.path.join(args.out, "calendar.csv"))
    write_md(rows, os.path.join(args.out, "calendar.md"))
    write_postiz(rows, os.path.join(args.out, "postiz-ready.json"))

    print(f"✓ {len(rows)} peças agendadas a partir de {args.start}")
    print(f"  → {os.path.join(args.out, 'calendar.csv')}")
    print(f"  → {os.path.join(args.out, 'calendar.md')}")
    print(f"  → {os.path.join(args.out, 'postiz-ready.json')}")


if __name__ == "__main__":
    main()
