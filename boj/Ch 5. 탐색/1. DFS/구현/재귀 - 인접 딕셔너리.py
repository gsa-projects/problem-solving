from typing import TypeAlias, List, Dict, Set

Graph: TypeAlias = Dict[str, List[str]]
graph: Graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['B', 'C', 'G'],
    'F': ['G'],
    'G': ['D', 'E', 'F']
}

def dfs(graph: Graph, now: str, visited: Set[str]):
    visited.add(now)
    print(now, end=' ')

    for w in graph[now]:
        if w not in visited:
            dfs(graph, w, visited)

dfs(graph, 'A', set())
