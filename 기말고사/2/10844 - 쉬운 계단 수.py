n = int(input())
D = [[0]*12 for _ in range(n + 1)]
D[1][2:11] = [1] * 9

for i in range(2, n + 1):
    for j in range(1, 11):
        D[i][j] = (D[i - 1][j - 1] + D[i - 1][j + 1]) % 1_000_000_000

print(sum(D[n]) % 1_000_000_000)
