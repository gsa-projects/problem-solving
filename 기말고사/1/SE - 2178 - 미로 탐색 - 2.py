from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]     # note: '붙어서' 입력됨. split 아님. \n 주의.

def bfs(g, v: tuple[int, int]):
    visited = [[False] * m for _ in range(n)]
    visited[v[0]][v[1]] = True

    queue = deque([v])
    while queue:
        a, b = queue.popleft()

        for x, y in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
            if 0 <= x < n and 0 <= y < m:
                if not visited[x][y]:
                    if g[x][y] > 0:
                        queue.append((x, y))
                        visited[x][y] = True
                        g[x][y] = g[a][b] + 1

bfs(maze, (0, 0))
print(maze[n - 1][m - 1])
