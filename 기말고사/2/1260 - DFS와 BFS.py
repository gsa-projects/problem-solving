from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(g, v, V):
    V[v] = True
    print(v, end=' ')

    for w in sorted(g[v]):
        if not V[w]:
            dfs(g, w, V)

def bfs(g, v):
    visited = [False] * (n + 1)
    visited[v] = True

    queue = deque([v])
    while queue:
        top = queue.popleft()
        print(top, end=' ')

        for w in sorted(g[top]):
            if not visited[w]:
                queue.append(w)
                visited[w] = True

dfs(graph, v, [False] * (n + 1))
print()
bfs(graph, v)
