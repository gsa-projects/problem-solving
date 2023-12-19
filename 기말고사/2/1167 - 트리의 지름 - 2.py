from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    inp = list(map(int, input().split()))

    for i in range(1, len(inp) - 1, 2):
        graph[inp[0]].append((inp[i], inp[i + 1]))

def bfs(g, now):
    D = [-1] * (v + 1)
    D[now] = 0

    queue = deque([now])
    while queue:
        top = queue.popleft()

        for w, d in g[top]:
            if D[w] == -1:
                D[w] = D[top] + d
                queue.append(w)

    return D

D = bfs(graph, 1)
print(max(bfs(graph, D.index(max(D)))))
