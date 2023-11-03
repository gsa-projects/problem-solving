from collections import deque

indices = list(range(1, 8))
n = len(indices) + 1
edges = [(1, 2), (1, 3), (2, 3), (3, 5), (3, 6), (4, 5), (5, 7), (6, 7)]
graph = [[0] * n for _ in range(n)]

for v, w in edges:
    graph[v][w] = 1
    graph[w][v] = 1

def bfs(graph, start):
    visited = [False]*n
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for w in range(len(graph[v])):
            if graph[v][w]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True

bfs(graph, 3)   # 3 1 2 5 6 4 7
