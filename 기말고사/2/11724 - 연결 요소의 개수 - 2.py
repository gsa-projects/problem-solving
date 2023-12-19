from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(g, v, V):
    V[v] = True

    queue = deque([v])
    while queue:
        top = queue.popleft()

        for w in g[top]:    # note: g[v]라고 해서 헤맴
            if not V[w]:    # note: g[w]라고 해서 헤맴
                V[w] = True
                queue.append(w)

visited = [False] * (n + 1)
cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)
