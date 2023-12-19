n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(g, v, V):
    V[v] = True

    for w in g[v]:
        if not V[w]:
            dfs(g, w, V)

cnt = 0
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
