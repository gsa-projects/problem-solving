n = int(input())
T = [0] * n
P = [0] * n
D = [0] * (n + 1)

for i in range(n):
    T[i], P[i] = map(int, input().split())

for i in range(n - 1, -1, -1):
    if i + T[i] <= n:   # note: T[i]를 고려해서 range를 작성해 range(n, -1, -1) 했다가 T에서 IndexError
        D[i] = max(D[i + 1], D[i + T[i]] + P[i])
    else:
        D[i] = D[i + 1]

print(D[0])
