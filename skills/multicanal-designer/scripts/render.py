#!/usr/bin/env python3
"""
render.py — Renderiza arquivos HTML em imagens PNG na marca, usando o Chrome em
modo headless. É o núcleo determinístico do multicanal-designer: o agente compõe
o HTML (a partir dos templates + brand.css), este script rasteriza com pixel-perfect.

Por que Chrome headless e não uma lib de imagem: conteúdo de autoridade é
tipográfico (carrossel, post, thumbnail). HTML/CSS dá controle total de fonte,
cor de marca, layout e quebra de texto — e renderiza idêntico ao que se vê no
navegador. Sem dependência nativa (Chrome já está instalado).

Uso:
    # um arquivo
    python render.py slide.html --out slide.png --width 1080 --height 1350

    # uma pasta inteira (renderiza cada .html para .png ao lado)
    python render.py ./carrossel/ --width 1080 --height 1350

Opções:
    --width / --height  dimensões em px (default 1080x1350 — feed vertical IG)
    --scale             device scale factor (default 2 — saída crisp/retina)
    --out               caminho do PNG (só no modo arquivo único)
    --chrome            caminho do chrome.exe (auto-detecta se omitido)

Dimensões nativas comuns:
    Instagram feed vertical   1080 x 1350
    Instagram/LinkedIn quadr. 1080 x 1080
    YouTube thumbnail         1280 x 720
    TikTok/Reels/Stories      1080 x 1920
"""

import argparse
import glob
import os
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def find_chrome(explicit: str = None) -> str:
    if explicit:
        if os.path.isfile(explicit):
            return explicit
        sys.stderr.write(f"ERRO: chrome não encontrado em {explicit}\n")
        sys.exit(2)
    for c in CHROME_CANDIDATES:
        if os.path.isfile(c):
            return c
    sys.stderr.write(
        "ERRO: Chrome não encontrado. Passe --chrome <caminho do chrome.exe>\n"
    )
    sys.exit(2)


def render_one(chrome: str, html_path: str, png_path: str, w: int, h: int, scale: float) -> bool:
    html_abs = os.path.abspath(html_path)
    # file:// URL — barras normais funcionam no Chrome em qualquer SO
    url = "file:///" + html_abs.replace("\\", "/").lstrip("/")
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",        # evita lock se o Chrome já estiver aberto
            f"--force-device-scale-factor={scale}",
            f"--window-size={w},{h}",
            "--default-background-color=00000000",  # fundo transparente onde o CSS não pinta
            "--virtual-time-budget=3000",           # dá tempo de carregar web fonts antes do shot
            f"--screenshot={os.path.abspath(png_path)}",
            url,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if not os.path.isfile(png_path):
            sys.stderr.write(f"falha ao renderizar {html_path}\n{proc.stderr[:500]}\n")
            return False
    return True


def main():
    ap = argparse.ArgumentParser(description="Renderiza HTML em PNG via Chrome headless.")
    ap.add_argument("input", help="Arquivo .html OU pasta com .html")
    ap.add_argument("--out", help="PNG de saída (modo arquivo único)")
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1350)
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--chrome", help="Caminho do chrome.exe")
    args = ap.parse_args()

    chrome = find_chrome(args.chrome)

    if os.path.isdir(args.input):
        htmls = sorted(glob.glob(os.path.join(args.input, "*.html")))
        if not htmls:
            sys.stderr.write(f"nenhum .html em {args.input}\n")
            sys.exit(1)
        ok = 0
        for hp in htmls:
            pp = os.path.splitext(hp)[0] + ".png"
            if render_one(chrome, hp, pp, args.width, args.height, args.scale):
                print(f"✓ {os.path.basename(pp)}")
                ok += 1
        print(f"\n{ok}/{len(htmls)} renderizados em {args.input} ({args.width}x{args.height} @{args.scale}x)")
    else:
        if not os.path.isfile(args.input):
            sys.stderr.write(f"arquivo não encontrado: {args.input}\n")
            sys.exit(1)
        out = args.out or (os.path.splitext(args.input)[0] + ".png")
        out_dir = os.path.dirname(out)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        if render_one(chrome, args.input, out, args.width, args.height, args.scale):
            print(f"✓ {out} ({args.width}x{args.height} @{args.scale}x)")
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
