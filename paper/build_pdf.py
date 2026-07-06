"""Gera o PDF do artigo a partir do Markdown em `paper/`.

Pipeline: reembute as 9 figuras (base64) a partir dos PNGs atuais em `graphs/`,
converte o Markdown em HTML pronto para impressão e renderiza o PDF com o
Google Chrome em modo headless. Reembutir as figuras mantém o `.md`
autocontido e coerente com os dados regenerados por `src/experiments.py`.

Requer `markdown` (ver requirements.txt) e uma instalação do Google Chrome ou
Chromium. Rode a partir da raiz do projeto (ou de qualquer lugar — os caminhos
são resolvidos em relação a este arquivo):

    python paper/build_pdf.py                # gera paper/paper_revisado.pdf
    python paper/build_pdf.py paper_v1.md    # gera paper/paper_v1.pdf

O reembutimento das figuras só é feito para o `paper_revisado.md`: os PNGs de
`graphs/` refletem os dados atuais, que correspondem à versão revisada. O
`paper_v1.md` é um registro histórico — suas figuras embutidas (da bateria de
medição original) são preservadas, apenas renderizadas em PDF.

Atenção: a exportação do Google Docs reduziu as figuras do `paper_v1.md` a
miniaturas (~170×128 px); um PDF gerado a partir dele sai com figuras de baixa
resolução. O `paper_v1.pdf` versionado é a exportação em resolução plena do
próprio Google Docs — prefira mantê-lo a regenerá-lo por este script.
"""

import base64
import re
import shutil
import subprocess
import sys
from pathlib import Path


PAPER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PAPER_DIR.parent
GRAPHS_DIR = PROJECT_ROOT / "graphs"
DEFAULT_MD = "paper_revisado.md"

# Ordem das figuras no relatório: Fig.1 nós visitados, Fig.2 tempo, Fig.3 custo,
# cada uma com as colunas 10% / 20% / 30%.
IMAGE_MAP = {
    "image1": "visited_nodes_10.png", "image2": "visited_nodes_20.png", "image3": "visited_nodes_30.png",
    "image4": "runtime_10.png",       "image5": "runtime_20.png",       "image6": "runtime_30.png",
    "image7": "path_cost_10.png",     "image8": "path_cost_20.png",     "image9": "path_cost_30.png",
}

# Candidatos de executável do Chrome/Chromium por plataforma.
CHROME_CANDIDATES = [
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 1.8cm 1.9cm; }
* { box-sizing: border-box; }
body { font-family: "Times New Roman", Georgia, serif; font-size: 10.5pt;
       line-height: 1.4; color: #111; }
p { text-align: justify; margin: 0.5em 0; }
strong { font-weight: bold; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }
th, td { border: 0.5pt solid #999; padding: 3px 6px; text-align: center; vertical-align: middle; }
/* Tabelas usadas só para dispor figuras (células apenas com imagem): sem borda. */
td:has(img) { border: none; padding: 2px; }
tr:has(img) td { border: none; }
img { max-width: 100%; height: auto; display: block; margin: 0 auto; }
em { color: #333; font-size: 9pt; }
"""

HTML_TEMPLATE = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>{css}</style></head>
<body>{body}</body></html>"""


def data_uri(png_name):
    """Lê um PNG de `graphs/` e devolve seu conteúdo como data URI base64."""
    raw = (GRAPHS_DIR / png_name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii")


def refresh_images(text):
    """Reescreve cada definição `[imageN]: data:...` com o PNG atual."""
    for name, png in IMAGE_MAP.items():
        text = re.sub(
            rf"^\[{name}\]:.*$",
            f"[{name}]: {data_uri(png)}",
            text,
            flags=re.MULTILINE,
        )
    return text


def find_chrome():
    """Localiza um executável do Chrome/Chromium ou encerra com instrução."""
    for candidate in CHROME_CANDIDATES:
        resolved = shutil.which(candidate) if "/" not in candidate and "\\" not in candidate else candidate
        if resolved and Path(resolved).exists():
            return resolved
    sys.exit(
        "Chrome/Chromium não encontrado. Instale o Google Chrome ou ajuste "
        "CHROME_CANDIDATES em paper/build_pdf.py."
    )


def main():
    try:
        import markdown
    except ImportError:
        sys.exit("Módulo 'markdown' ausente. Rode: pip install -r requirements.txt")

    report_md = PAPER_DIR / (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MD)
    if not report_md.exists():
        sys.exit(f"Arquivo não encontrado: {report_md}")

    text = report_md.read_text(encoding="utf-8")
    # Só a versão revisada acompanha os dados atuais de graphs/; o paper_v1 é
    # um registro histórico e mantém as figuras da bateria de medição original.
    if report_md.name == DEFAULT_MD:
        text = refresh_images(text)
        report_md.write_text(text, encoding="utf-8")  # mantém o .md autocontido

    body = markdown.markdown(text, extensions=["tables", "attr_list", "md_in_html"])
    html = HTML_TEMPLATE.format(css=CSS, body=body)

    html_path = PAPER_DIR / "_report.html"
    pdf_path = report_md.with_suffix(".pdf")
    html_path.write_text(html, encoding="utf-8")

    chrome = find_chrome()
    subprocess.run(
        [
            chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    html_path.unlink(missing_ok=True)

    print(f"PDF gerado em {pdf_path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
