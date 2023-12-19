n = int(input())
T = [0] * n
P = [0] * n

for i in range(n):
    T[i], P[i] = map(int, input().split())

max_cost = 0
def dfs(day, cost):
    if day >= n:    # note: day + T[day] > n 이라고 했다가 틀림. 어차피 이 조건은 if에 의해서 무력화되고 dfs(day+1)에 의해 넘길걸 고려했어야 했음
        global max_cost
        max_cost = max(cost, max_cost)
        return

    if day + T[day] <= n:
        dfs(day + T[day], cost + P[day])
    dfs(day + 1, cost)

dfs(0, 0)
print(max_cost)
