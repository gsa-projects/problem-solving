n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(g, v, visited, d):
    if d == 4:
        print(1)
        exit()

    visited[v] = True

    for w in g[v]:
        if not visited[w]:
            dfs(g, w, visited, d + 1)

    # note: 백트래킹 위치는 모든 경로를 다 분석하고 나서.
    #  성곽 문제에서도 (변경 -> bfs 콜 -> 백트래킹 이렇게 함. 이것도 dfs 끝나고 백트래킹이니 동일)
    visited[v] = False

for i in range(n):
    dfs(graph, i, [False] * n, 0)
print(0)
