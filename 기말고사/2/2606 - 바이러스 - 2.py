from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(g, v):
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 0

    queue = deque([v])
    while queue:
        top = queue.popleft()

        for w in g[top]:
            if not visited[w]:
                cnt += 1
                queue.append(w)
                visited[w] = True

    return cnt

print(bfs(graph, 1))
