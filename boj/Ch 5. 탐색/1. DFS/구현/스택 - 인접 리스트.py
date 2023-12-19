Graph = list[list[int]]
Visited = list[bool]

graph: Graph = [
    [],
    [2, 3, 4],
    [1, 4],
    [1, 4],
    [1, 2, 3]
]

# graph = [
#     [],
#     [2, 3],
#     [1, 3],
#     [1, 2, 5, 6],
#     [5],
#     [3, 4, 7],
#     [3, 7],
#     [5, 6]
# ]

def dfs_recursive(g: Graph, v: int, V: Visited):
    V[v] = True
    print(v, end=' ')

    for w in sorted(g[v]):
        if not V[w]:
            dfs_recursive(g, w, V)

def dfs_stack(g: Graph, v: int):
    visited = [False] * len(g)

    stack = [v]
    visited[v] = True
    print(v, end=' ')

    while stack:
        back = True

        for w in sorted(g[stack[-1]]):
            if not visited[w]:
                back = False

                stack.append(w)
                visited[w] = True
                print(w, end=' ')

                break

        if back:
            stack.pop()

def dfs_stack2(g: Graph, v: int):
    visited = [False] * len(g)

    stack = [v]
    visited[v] = True

    while stack:
        top = stack.pop()
        print(top, end=' ')

        for w in sorted(g[top], reverse=True):
            if not visited[w]:
                stack.append(w)
                visited[w] = True

dfs_recursive(graph, 1, [False] * len(graph))
print()
dfs_stack(graph, 1)
print()
dfs_stack2(graph, 1)
