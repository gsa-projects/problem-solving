__problem__ = 'https://boj.kr/2178', '미로 탐색'

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 인접 리스트도, 인접 행렬도 아님
# note: input 함수가 지금 readline이라서 역슬래쉬가 포함되는 걸 생각해야함
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

def bfs(g, s: tuple[int, int]):
    # n, m = len(g), len(g[0])  를 쓰긴 하셨는데 필요 없음
    visited = [[False] * m for _ in range(n)]

    visited[s[0]][s[1]] = True
    q = deque([s])

    while q:
        a, b = q.popleft()

        # 인접한 정점들 탐색
        for x, y in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
            # 이 인접한 정점이 존재하는지 확인
            if 0 <= x < n and 0 <= y < m:
                # 이 인접한 정점이 벽이 아닌지 (통과 가능한지) 확인

                # 여기서 어차피 통과 가능한 정점들은 아직 값이 0 or 1에서 바뀌지 않아서 g[x][y] == 1 해도 작동은 함,
                # 그래도 g의 값이 0을 제외하고는 결국 다 바뀐다는 것을 고려해서 g[x][y] != 0를 명시적으로 써주는 것이 가독성을 올림
                if g[x][y] != 0:
                    # 이 인접한 정점이 이미 방문했는지 확인
                    if not visited[x][y]:
                        visited[x][y] = True
                        g[x][y] = g[a][b] + 1
                        q.append((x, y))

bfs(maze, (0, 0))
print(maze[n-1][m-1])
