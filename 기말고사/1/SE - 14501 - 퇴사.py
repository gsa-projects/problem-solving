n = int(input())
T = [0] * n
P = [0] * n

for i in range(n):
    T[i], P[i] = map(int, input().split())

ans = 0

def dfs(i, cost):
    global ans

    if i >= n:
        ans = max(ans, cost)
        return

    if i + T[i] <= n:
        dfs(i + T[i], cost + P[i])
    dfs(i + 1, cost)

dfs(0, 0)
print(ans)
