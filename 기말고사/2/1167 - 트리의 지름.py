v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    inp = list(map(int, input().split()))

    for i in range(1, len(inp) - 1, 2):
        graph[inp[0]].append((inp[i], inp[i + 1]))

def dfs(g, now):      # note: v랑 로컬 v랑 이름 겹쳤음
    D = [-1] * (v + 1)
    D[now] = 0

    stack = [now]
    while stack:
        top = stack.pop()

        for w, d in g[top]:
            if D[w] == -1:
                D[w] = D[top] + d
                stack.append(w)

    return D

D = dfs(graph, 1)
print(max(dfs(graph, D.index(max(D)))))
