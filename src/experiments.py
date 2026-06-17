import csv
import time

from grid import generate_grid, get_neighbors
from dijkstra import dijkstra
from astar import astar


def measure(algorithm, grid, start, goal):
    start_time = time.perf_counter()
    result = algorithm(grid, start, goal, get_neighbors)
    end_time = time.perf_counter()

    result["runtime_ms"] = (end_time - start_time) * 1000
    return result


def run_experiments():
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

    with open("results/results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run_experiments()