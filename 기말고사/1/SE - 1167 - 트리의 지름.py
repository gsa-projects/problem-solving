v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    inp = list(map(int, input().split()))
    for i in range(1, len(inp) - 1, 2):
        graph[inp[0]].append((inp[i], inp[i + 1]))

def dfs(g, v, D):
    for w, d in g[v]:
        if D[w] == -1:
            D[w] = D[v] + d
            dfs(g, w, D)

D = [-1] * (v + 1)
D[1] = 0
dfs(graph, 1, D)

u = D.index(max(D))
D = [-1] * (v + 1)
D[u] = 0
dfs(graph, u, D)

print(max(D))
