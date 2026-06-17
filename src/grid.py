import random


def generate_grid(size, obstacle_rate, seed=None):
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