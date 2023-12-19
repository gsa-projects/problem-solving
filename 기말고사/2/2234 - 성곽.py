from collections import deque

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

def bfs(i_, j_):
    visited[i_][j_] = True
    cnt = 1     # note: 처음부터 방 하나 포함

    queue = deque([(i_, j_)])   # note: deque((i, j)) 가 아니고 deque([(i, j)])
    while queue:
        i, j = queue.popleft()
        bin = A[i][j]

        ways = []
        if not bin & 1:
            ways.append((i, j - 1))
        if not bin & 2:
            ways.append((i - 1, j))
        if not bin & 4:
            ways.append((i, j + 1))
        if not bin & 8:
            ways.append((i + 1, j))

        for a, b in ways:
            if 0 <= a < m and 0 <= b < n:
                if not visited[a][b]:   # note: visit을 나중에 체크해야 여기서 KeyError가 안나지 이놈아
                    visited[a][b] = True
                    queue.append((a, b))
                    cnt += 1

    return cnt      # note: 들여쓰기 실수로 for 끝나고 리턴됨

max_room = 0
cnt = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            max_room = max(max_room, bfs(i, j))
            cnt += 1

print(cnt)
print(max_room)

visited = [[False] * n for _ in range(m)]
max_room2 = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            w = 1
            while A[i][j] >= w:
                A[i][j] -= w
                max_room2 = max(max_room2, bfs(i, j))
                visited = [[False] * n for _ in range(m)]
                A[i][j] += w
                w *= 2

print(max_room2)
