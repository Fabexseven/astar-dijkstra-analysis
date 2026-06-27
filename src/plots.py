"""Gera os gráficos comparativos a partir de `results/results.csv`.

Produz, para cada taxa de obstáculo (10%, 20%, 30%), três PNGs em `graphs/`:
custo do caminho, nós visitados e tempo de execução — cada um com média ±
desvio padrão em função do tamanho do grid.

Pode ser executado a partir da raiz do projeto:

    python -m src.plots
    # ou
    python src/plots.py
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Raiz do projeto (um nível acima de `src/`) — usada para localizar `results/`
# e `graphs/` independentemente do diretório de onde o script é chamado.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_PATH = PROJECT_ROOT / "results" / "results.csv"
GRAPHS_DIR = PROJECT_ROOT / "graphs"


def load_summary():
    """Carrega o CSV de resultados e devolve estatísticas agregadas."""
    df = pd.read_csv(RESULTS_PATH)
    df = df[df["found"] == True]

    return (
        df.groupby(["size", "obstacle_rate", "algorithm"])
        .agg(
            path_cost_mean=("path_cost", "mean"),
            path_cost_std=("path_cost", "std"),
            visited_nodes_mean=("visited_nodes", "mean"),
            visited_nodes_std=("visited_nodes", "std"),
            runtime_ms_mean=("runtime_ms", "mean"),
            runtime_ms_std=("runtime_ms", "std"),
        )
        .reset_index()
    )


def plot_metric(summary, metric, ylabel, filename):
    """Gera um PNG por taxa de obstáculo para a métrica indicada."""
    for obstacle_rate in sorted(summary["obstacle_rate"].unique()):
        data = summary[summary["obstacle_rate"] == obstacle_rate]

        plt.figure()

        for algorithm in sorted(data["algorithm"].unique()):
            alg_data = data[data["algorithm"] == algorithm]

            plt.errorbar(
                alg_data["size"],
                alg_data[f"{metric}_mean"],
                yerr=alg_data[f"{metric}_std"],
                marker="o",
                capsize=4,
                label=algorithm,
            )

        plt.xlabel("Tamanho do mapa")
        plt.ylabel(ylabel)
        plt.title(f"{ylabel} - Obstáculos {int(obstacle_rate * 100)}%")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(
            GRAPHS_DIR / f"{filename}_{int(obstacle_rate * 100)}.png",
            dpi=300,
        )
        plt.close()


def main():
    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    summary = load_summary()

    plot_metric(summary, "visited_nodes", "Nós visitados", "visited_nodes")
    plot_metric(summary, "runtime_ms", "Tempo de execução (ms)", "runtime")
    plot_metric(summary, "path_cost", "Custo do caminho", "path_cost")

    print(f"Gráficos gerados em {GRAPHS_DIR.relative_to(PROJECT_ROOT)}/")


if __name__ == "__main__":
    main()
