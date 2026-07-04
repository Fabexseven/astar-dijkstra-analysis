# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An academic empirical study (Unisinos, Análise de Algoritmos) comparing **Dijkstra** (baseline) and **A\*** for shortest-path on 2D grids with random obstacles. Both algorithms are implemented from scratch — no external graph libraries. The deliverable is the experimental data (`results/results.csv`), the comparison plots (`graphs/`), and a report (`paper/`). Code comments and docstrings are written in **Portuguese**; keep that convention when editing. The paper itself is also in Portuguese.

Non-code folders:

- `paper/` — the article in two versions: `paper_v1.{md,pdf}` (original) and `paper_revisado.{md,pdf}` (**the current deliverable** — edit this one). Also holds `review-*.md`, LLM-generated conformity reviews (no suffix = review of v1; `-TR` suffix = review of the revised version) — these are historical records, don't edit them.
- `prompts/` — the versioned evaluation prompt used to generate those reviews.
- `docs/` — reference PDFs: the assignment (`TrabalhoI.pdf`) and the three cited papers (Hart/Nilsson/Raphael 1968 = ref. [1], Ardiansyah et al. 2025 = ref. [2], Dijkstra 1959 = ref. [3]).

## Commands

Run everything from the **project root** (the `-m` form is canonical; scripts also self-add `src/` to the path so `python src/...` works too):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python -m src.experiments   # (re)generates results/results.csv — 540 rows + header
python -m src.plots         # reads the CSV, writes 9 PNGs to graphs/
python -m src.significance  # reads the CSV, writes results/significance.csv + prints a table
python paper/build_pdf.py   # re-embeds the 9 PNGs (base64) into paper_revisado.md and renders paper_revisado.pdf via headless Chrome
```

There is no test suite or linter. `experiments.py` must run before `plots.py` and `significance.py` (both read the CSV it writes); `build_pdf.py` reads `graphs/` and requires Google Chrome or Chromium installed. It takes an optional target (`python paper/build_pdf.py paper_v1.md`) but only refreshes images for `paper_revisado.md`. **Do not regenerate `paper_v1.pdf`**: the Docs export left only ~170×128 thumbnails in `paper_v1.md`, so a rebuild degrades the figures — the committed PDF is the full-resolution Docs export.

## Architecture

The pipeline is **algorithms → experiment harness → CSV → plots**, with a deliberate contract between the layers:

- `src/grid.py` — `generate_grid(size, rate, seed)` returns `(grid, start, goal)` with `(0,0)`→`(n-1,n-1)` forced free; `get_neighbors` gives 4-connected free cells. The `seed` makes obstacle layouts reproducible.
- `src/dijkstra.py` and `src/astar.py` — **share the same signature** `(grid, start, goal, get_neighbors)` and **return the same dict** (`path_cost`, `visited_nodes`, `found`). A\* only differs by priority `f = g + h` with `manhattan` heuristic. Preserve this identical interface — `experiments.py` swaps the two interchangeably in a loop. Edge cost is fixed at 1.
- `src/experiments.py` — nested loop over sizes `[50,100,200]` × rates `[0.1,0.2,0.3]` × seeds `0..29` × both algorithms = 540 runs. `measure()` runs each call `TIMING_REPETITIONS` (=10) times with `time.perf_counter` and records the **median** as `runtime_ms` (robust to OS/warm-up noise; `path_cost`/`visited_nodes` are deterministic so the result dict is identical across reps). Writes the CSV with `csv.DictWriter` keyed off the first row's keys.
- `src/plots.py` — pandas/matplotlib; filters to `found == True`, groups by `(size, obstacle_rate, algorithm)`, plots mean ± std vs. grid size. Emits three metrics × three obstacle rates = 9 PNGs at 300 dpi.
- `src/significance.py` — pandas/scipy; pairs Dijkstra vs A\* `runtime_ms` by `(size, obstacle_rate, seed)` (keeping only seeds solvable by both) and runs a paired **Wilcoxon signed-rank** test per configuration (paired t-test as a secondary check). Writes `results/significance.csv` and prints a table. SciPy is an auxiliary-analysis dependency only — the algorithms themselves stay hand-written.

Paths are resolved via `PROJECT_ROOT = Path(__file__).resolve().parent.parent` in both `experiments.py` and `plots.py`, so `results/` and `graphs/` are found regardless of the caller's working directory.

## Conventions to maintain

- `path_cost` and `visited_nodes` are **deterministic per seed**; only `runtime_ms` varies by machine. The README's results numbers assume the committed CSV — note in any report that re-running overwrites it.
- If you add a metric, thread it through all three layers: the algorithm's return dict → the row dict in `experiments.py` → the agg/plot calls in `plots.py`.
