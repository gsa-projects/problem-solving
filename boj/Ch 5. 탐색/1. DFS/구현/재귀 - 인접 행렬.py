from typing import TypeAlias, List

vertices = list(range(1, 7+1))
edges = [(1, 2), (1, 3), (2, 3), (3, 5), (3, 6), (4, 5), (5, 7), (6, 7)]
le = len(vertices) + 1

Graph: TypeAlias = List[List[int]]
graph: Graph = [[0] * le for _ in range(le)]

for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph: Graph, now: int, visited: List[int]):
    visited[now] = True
    print(now, end=' ')

    for w in range(len(graph[now])):    # 인접 행렬은 어차피 정사각형이라 range(len(graph)) 해도 됨, 쌤은 range(1, len(graph))
        if graph[now][w]:   # 인접 행렬은 두 정점의 연결 유무도 봐야 함
            if not visited[w]:
                dfs(graph, w, visited)

dfs(graph, 3, [False] * le)
