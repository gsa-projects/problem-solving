from collections import deque

graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'E'],
  'D': ['B', 'G'],
  'E': ['B', 'C', 'G'],
  'F': ['G'],
  'G': ['D', 'E', 'F']
}

def bfs(graph, start):
    visited = set()
    visited.add(start)
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for w in graph[v]:
            if w not in visited:
                queue.append(w)
                visited.add(w)

bfs(graph, 'A')     # A B C D E G F
