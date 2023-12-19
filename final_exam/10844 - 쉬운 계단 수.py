n = int(input())
pad = 1
D = [[0] * (pad + 10 + pad) for _ in range(n+1)]
D[1][1+pad:10+pad] = [1] * 9    # 0 제외 1~9는 시작부터 1개씩 존재

for i in range(2, n+1):
    for j in range(0+pad, 9+1+pad):
        D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % 1000000000

print(sum(D[n]) % 1000000000)
