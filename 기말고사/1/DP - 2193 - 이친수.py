n = int(input())
D = [[0, 0] for _ in range(n + 1)]

D[1][0] = 0
D[1][1] = 1

for i in range(2, n + 1):
    # 0은 1, 0 둘 다에서 올 수 있음
    D[i][0] = sum(D[i - 1])     # D[i - 1][0] + D[i - 1][1]

    # 1은 0에서만 올 수 있음
    D[i][1] = D[i - 1][0]

print(sum(D[n]))
