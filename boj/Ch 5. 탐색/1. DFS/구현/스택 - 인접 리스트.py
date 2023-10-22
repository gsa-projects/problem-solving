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

def dfs(graph: Graph, now: int):
    visited = [False] * len(graph)

    stack = [now]
    visited[now] = True
    print(now, end=' ')

    while stack:
        back = True

        for w in graph[stack[-1]]:
            if not visited[w]:
                back = False

                stack.append(w)
                visited[w] = True
                print(w, end=' ')

                break       # tqqqqqqqqqqqqq

        if back:
            stack.pop()

def dfs_enhanced(graph: Graph, now: int):
    visited = [False] * len(graph)

    stack = [now]
    visited[now] = True

    while stack:
        top = stack.pop()
        print(top, end=' ')

        for w in reversed(graph[top]):      # 쌤은 sorted(reverse=True) 으로 하심
            if not visited[w]:
                stack.append(w)
                visited[w] = True

dfs(graph, 3)
print()
dfs_enhanced(graph, 3)
