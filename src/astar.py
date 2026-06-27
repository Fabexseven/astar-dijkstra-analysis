"""Algoritmo A* com heurística de Manhattan para menor caminho em grid 2D."""

import heapq


def manhattan(a, b):
    """Distância de Manhattan — admissível e consistente para grids 4-conectados."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal, get_neighbors):
    """Executa A* de `start` até `goal` em `grid`.

    Usa `f = g + h`, onde `g` é o custo acumulado e `h` é a distância de
    Manhattan até `goal`. Retorna custo do caminho, número de nós visitados e
    se o objetivo foi alcançado — mesmo formato do `dijkstra` para facilitar
    a comparação.
    """
    queue = [(0, start)]
    g_score = {start: 0}
    visited = set()

    while queue:
        _, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan(neighbor, goal)
                heapq.heappush(queue, (f_score, neighbor))

    path_cost = g_score.get(goal, None)

    return {
        "path_cost": path_cost,
        "visited_nodes": len(visited),
        "found": path_cost is not None
    }
