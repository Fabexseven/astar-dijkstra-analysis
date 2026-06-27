"""Bateria de experimentos comparando Dijkstra e A*.

Para cada combinação de tamanho × densidade de obstáculos × seed, gera um
grid, executa os dois algoritmos, mede o tempo e salva uma linha no CSV de
resultados (`results/results.csv`).

Pode ser executado a partir da raiz do projeto:

    python -m src.experiments
    # ou
    python src/experiments.py
"""

import csv
import sys
import time
from pathlib import Path

# Permite `python src/experiments.py` (sem o `-m`) — adiciona `src/` ao path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from grid import generate_grid, get_neighbors
from dijkstra import dijkstra
from astar import astar


# Raiz do projeto (um nível acima de `src/`) — usada para localizar `results/`
# independentemente do diretório de onde o script é chamado.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_PATH = PROJECT_ROOT / "results" / "results.csv"


def measure(algorithm, grid, start, goal):
    """Executa `algorithm` cronometrando o tempo total em milissegundos."""
    start_time = time.perf_counter()
    result = algorithm(grid, start, goal, get_neighbors)
    end_time = time.perf_counter()

    result["runtime_ms"] = (end_time - start_time) * 1000
    return result


def run_experiments():
    """Roda toda a grade experimental e escreve o CSV de resultados."""
    sizes = [50, 100, 200]
    obstacle_rates = [0.1, 0.2, 0.3]
    repetitions = 30

    rows = []

    for size in sizes:
        for obstacle_rate in obstacle_rates:
            for seed in range(repetitions):
                grid, start, goal = generate_grid(size, obstacle_rate, seed)

                for name, algorithm in [
                    ("Dijkstra", dijkstra),
                    ("A*", astar),
                ]:
                    result = measure(algorithm, grid, start, goal)

                    rows.append({
                        "algorithm": name,
                        "size": size,
                        "obstacle_rate": obstacle_rate,
                        "seed": seed,
                        "found": result["found"],
                        "path_cost": result["path_cost"],
                        "visited_nodes": result["visited_nodes"],
                        "runtime_ms": result["runtime_ms"],
                    })

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Resultados salvos em {RESULTS_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    run_experiments()
