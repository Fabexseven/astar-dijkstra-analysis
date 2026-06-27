"""Algoritmo de Dijkstra para menor caminho em grid 2D (usado como baseline)."""

import heapq


def dijkstra(grid, start, goal, get_neighbors):
    """Executa Dijkstra de `start` até `goal` em `grid`.

    Cada aresta tem custo 1 (grid uniforme). Retorna um dicionário com o custo
    do caminho, o número de nós visitados e se o objetivo foi alcançado.
    """
    queue = [(0, start)]
    distances = {start: 0}
    visited = set()
    came_from = {}

    while queue:
        cost, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            new_cost = cost + 1

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(queue, (new_cost, neighbor))

    path_cost = distances.get(goal, None)

    return {
        "path_cost": path_cost,
        "visited_nodes": len(visited),
        "found": path_cost is not None
    }
