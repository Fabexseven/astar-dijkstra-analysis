import heapq

def dijkstra(grid, start, goal, get_neighbors):
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