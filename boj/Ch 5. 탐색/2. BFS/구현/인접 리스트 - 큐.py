from collections import deque

graph = [
    [],
    [2, 3],
    [1, 3],
    [1, 2, 5, 6],
    [5],
    [3, 4, 7],
    [3, 7],
    [5, 6],
]

def bfs(graph, start):
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True

bfs(graph, 3)   # 3 1 2 5 6 4 7
