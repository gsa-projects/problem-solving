n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(g, v, V):
    V[v] = True

    for w in g[v]:
        if not V[w]:    # note: V[v] 라고 해서 헤맴
            dfs(g, w, V)

visited = [False] * (n + 1)
cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)
