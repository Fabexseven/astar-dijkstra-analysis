"""Teste de significância pareado entre Dijkstra e A* nos tempos de execução.

Para cada configuração (tamanho x densidade de obstáculos), pareia os tempos de
Dijkstra e A* pelas mesmas sementes e aplica o teste de Wilcoxon de postos
sinalizados (pareado, não paramétrico). Isso permite afirmar se a diferença de
tempo observada é estatisticamente significativa, e não apenas ruído de medição
— particularmente importante nos cenários esparsos, em que o A* é apenas
marginalmente mais lento. Um teste t pareado é reportado como verificação
complementar.

O pareamento por semente é possível porque Dijkstra e A* são avaliados sobre os
mesmos mapas; instâncias sem caminho viável são descartadas simultaneamente nos
dois algoritmos. Só é necessário `results/results.csv` — o uso de SciPy aqui é
tarefa auxiliar de análise, não substitui os algoritmos, implementados do zero.

Requer que o CSV já exista (rode antes `python -m src.experiments`):

    python -m src.significance
    # ou
    python src/significance.py
"""

from pathlib import Path

import pandas as pd
from scipy.stats import ttest_rel, wilcoxon


# Raiz do projeto (um nível acima de `src/`) — localiza `results/`
# independentemente do diretório de onde o script é chamado.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_PATH = PROJECT_ROOT / "results" / "results.csv"
SIGNIFICANCE_PATH = PROJECT_ROOT / "results" / "significance.csv"

# Nível de significância para rejeitar a hipótese nula (tempos iguais).
ALPHA = 0.05


def paired_runtimes(df):
    """Devolve os tempos de Dijkstra e A* pareados por (tamanho, densidade, seed).

    Mantém apenas as sementes em que ambos os algoritmos encontraram caminho.
    Retorna um DataFrame com colunas `Dijkstra` e `A*` (ms) indexado pela
    configuração e pela semente.
    """
    df = df[df["found"] == True]

    pivot = df.pivot_table(
        index=["size", "obstacle_rate", "seed"],
        columns="algorithm",
        values="runtime_ms",
    ).dropna()

    return pivot


def run_tests():
    """Roda os testes pareados por configuração e escreve/retorna a tabela."""
    df = pd.read_csv(RESULTS_PATH)
    pivot = paired_runtimes(df)

    rows = []

    for (size, rate), group in pivot.groupby(level=["size", "obstacle_rate"]):
        dijkstra = group["Dijkstra"]
        astar = group["A*"]
        diff = astar - dijkstra  # negativo => A* mais rápido
        n = len(diff)

        # Wilcoxon (não paramétrico, principal) e teste t pareado (complementar).
        # Ambos exigem que as diferenças não sejam todas nulas.
        try:
            w_stat, w_p = wilcoxon(astar, dijkstra)
        except ValueError:
            w_stat, w_p = float("nan"), float("nan")

        try:
            t_stat, t_p = ttest_rel(astar, dijkstra)
        except (ValueError, ZeroDivisionError):
            t_stat, t_p = float("nan"), float("nan")

        significant = w_p < ALPHA
        if not significant:
            verdict = "sem diferença significativa"
        elif diff.median() < 0:
            verdict = "A* significativamente mais rápido"
        else:
            verdict = "A* significativamente mais lento"

        rows.append({
            "size": size,
            "obstacle_rate": rate,
            "n": n,
            "dijkstra_median_ms": round(dijkstra.median(), 3),
            "astar_median_ms": round(astar.median(), 3),
            "median_diff_ms": round(diff.median(), 3),
            "ratio_astar_dij": round(astar.mean() / dijkstra.mean(), 3),
            "wilcoxon_stat": round(w_stat, 3),
            "wilcoxon_p": w_p,
            "ttest_p": t_p,
            "significant": significant,
            "verdict": verdict,
        })

    return pd.DataFrame(rows)


def format_table(result):
    """Formata a tabela de resultados para leitura no terminal."""
    lines = [
        f"Teste de Wilcoxon pareado (A* vs Dijkstra) — alpha = {ALPHA}",
        f"n = sementes com caminho viável nos dois algoritmos.",
        "",
        f"{'tam':>4} {'obst':>5} {'n':>3} "
        f"{'Dij(md)':>8} {'A*(md)':>8} {'dif(md)':>8} {'raz':>5} "
        f"{'W':>7} {'p(Wilc)':>9} {'p(t)':>9}  veredito",
    ]

    for _, r in result.iterrows():
        lines.append(
            f"{int(r['size']):>4} "
            f"{int(r['obstacle_rate'] * 100):>4}% "
            f"{int(r['n']):>3} "
            f"{r['dijkstra_median_ms']:>8.2f} "
            f"{r['astar_median_ms']:>8.2f} "
            f"{r['median_diff_ms']:>8.2f} "
            f"{r['ratio_astar_dij']:>5.2f} "
            f"{r['wilcoxon_stat']:>7.1f} "
            f"{r['wilcoxon_p']:>9.2e} "
            f"{r['ttest_p']:>9.2e}  "
            f"{r['verdict']}"
        )

    return "\n".join(lines)


def main():
    result = run_tests()

    SIGNIFICANCE_PATH.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(SIGNIFICANCE_PATH, index=False)

    print(format_table(result))
    print(f"\nTabela salva em {SIGNIFICANCE_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
