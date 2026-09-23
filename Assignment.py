from collections import deque

grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start, goal = (0, 0), (5, 5)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0

    while queue:
        current, path = queue.popleft()
        expanded += 1

        if current == goal:
            return path, len(path) - 1, expanded

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None, float('inf'), expanded

path, cost, expanded = bfs()
print("BFS -> Жол:", path)
print("Құны:", cost, "| Кеңейтілген түйіндер:", expanded)



grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start, goal = (0, 0), (5, 5)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs():
    stack = [([start], 0)]
    visited = set()
    expanded = 0

    while stack:
        path, cost = stack.pop()
        current = path[-1]

        if current == goal:
            return path, cost, expanded

        if current not in visited:
            visited.add(current)
            expanded += 1

            r, c = current
            for dr, dc in reversed(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
                    stack.append((path + [(nr, nc)], cost + 1))
    return None, float('inf'), expanded

path, cost, expanded = dfs()
print("DFS -> Жол:", path)
print("Құны:", cost, "| Кеңейтілген түйіндер:", expanded)




import heapq

grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start, goal = (0, 0), (5, 5)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def ucs():
    pq = [(0, start, [start])]
    visited_costs = {start: 0}
    expanded = 0

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited_costs and cost > visited_costs[current]:
            continue

        expanded += 1

        if current == goal:
            return path, cost, expanded

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
                new_cost = cost + 1
                if (nr, nc) not in visited_costs or new_cost < visited_costs[(nr, nc)]:
                    visited_costs[(nr, nc)] = new_cost
                    heapq.heappush(pq, (new_cost, (nr, nc), path + [(nr, nc)]))
    return None, float('inf'), expanded

path, cost, expanded = ucs()
print("UCS -> Жол:", path)
print("Құны:", cost, "| Кеңейтілген түйіндер:", expanded)



import heapq

# 1. Торды (Grid) анықтау
grid = [
    ['S', '#', '.', '#', '.', '.'],#(4,3),(1,0)
    ['.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 5)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Тор ішінде ме және кедергі емес пе екенін тексеру функциясы
def is_valid(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

# Манхэттен эвристикасы: h(n) = |r1 - r2| + |c1 - c2|
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* алгоритмі
def a_star(grid, start, goal):
    # Priority queue форматы: (f_score, g_score, current_node, path)
    pq = [(heuristic(start, goal), 0, start, [start])]
    g_scores = {start: 0}
    expanded_nodes = 0

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in g_scores and g > g_scores[current]:
            continue

        expanded_nodes += 1

        # Мақсатты нүктеге жеткенін тексеру
        if current == goal:
            return path, g, expanded_nodes

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                new_g = g + 1
                if (nr, nc) not in g_scores or new_g < g_scores[(nr, nc)]:
                    g_scores[(nr, nc)] = new_g
                    new_f = new_g + heuristic((nr, nc), goal)
                    heapq.heappush(pq, (new_f, new_g, (nr, nc), path + [(nr, nc)]))

    return None, float('inf'), expanded_nodes

# Функцияны іске қосу және нәтижелерді шығару
path, cost, expanded = a_star(grid, start, goal)

print("--- A* Алгоритмінің нәтижесі ---")
print("Табылған жол:", path)
print("Жол құны (Cost):", cost)
print("Кеңейтілген түйіндер саны (Expanded nodes):", expanded)