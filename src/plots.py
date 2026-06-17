import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("graphs").mkdir(exist_ok=True)

df = pd.read_csv("results/results.csv")
df = df[df["found"] == True]

summary = (
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

def plot_metric(metric, ylabel, filename):
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
                label=algorithm
            )

        plt.xlabel("Tamanho do mapa")
        plt.ylabel(ylabel)
        plt.title(f"{ylabel} - Obstáculos {int(obstacle_rate * 100)}%")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"graphs/{filename}_{int(obstacle_rate * 100)}.png", dpi=300)
        plt.close()


plot_metric("visited_nodes", "Nós visitados", "visited_nodes")
plot_metric("runtime_ms", "Tempo de execução (ms)", "runtime")
plot_metric("path_cost", "Custo do caminho", "path_cost")

print("Gráficos gerados em /graphs")