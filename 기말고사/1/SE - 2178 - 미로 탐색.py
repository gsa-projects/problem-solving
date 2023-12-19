from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]     # note: '붙어서' 입력됨. split 아님. \n 주의.

def bfs(g, v: tuple[int, int]):
    visited = {v}
    queue = deque([v])

    while queue:
        a, b = queue.popleft()

        ways = []
        if 0 <= a - 1:
            ways.append((a - 1, b))
        if 0 <= b - 1:
            ways.append((a, b - 1))
        if a + 1 < n:
            ways.append((a + 1, b))
        if b + 1 < m:
            ways.append((a, b + 1))

        for w in ways:
            if w not in visited and g[w[0]][w[1]] > 0:
                queue.append(w)
                visited.add(w)
                g[w[0]][w[1]] = g[a][b] + 1

bfs(maze, (0, 0))
print(maze[n - 1][m - 1])
