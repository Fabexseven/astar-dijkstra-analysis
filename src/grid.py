"""Geração do grid 2D com obstáculos aleatórios e função de vizinhança."""

import random


def generate_grid(size, obstacle_rate, seed=None):
    """Gera um grid `size`x`size` com células livres (0) e obstáculos (1).

    A célula de início `(0, 0)` e de objetivo `(size-1, size-1)` são forçadas
    a ficarem livres. `seed` torna a geração reprodutível.
    """
    if seed is not None:
        random.seed(seed)

    grid = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_rate:
                grid[i][j] = 1

    start = (0, 0)
    goal = (size - 1, size - 1)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    return grid, start, goal


def get_neighbors(grid, node):
    """Retorna os vizinhos 4-conectados (cima/baixo/esquerda/direita) livres."""
    size = len(grid)
    x, y = node

    neighbors = []

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < size and 0 <= ny < size:
            if grid[nx][ny] == 0:
                neighbors.append((nx, ny))

    return neighbors
