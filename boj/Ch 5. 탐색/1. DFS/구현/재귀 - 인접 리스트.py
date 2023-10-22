from typing import TypeAlias, List

Graph: TypeAlias = List[List[int]]
graph: Graph = [
    [],
    [2, 3],
    [1, 3],
    [1, 2, 5, 6],
    [5],
    [3, 4, 7],
    [3, 7],
    [5, 6]
]

def dfs(graph: Graph, now: int, visited: List[int]):
    visited[now] = True
    print(now, end=' ')

    # 작은 수부터 순서대로 들어가고 싶다면, sorted(graph[now]) 하면 됨
    for w in graph[now]:
        if not visited[w]:
            dfs(graph, w, visited)

dfs(graph, 3, [False] * len(graph))
