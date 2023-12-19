n = int(input())
D = {1: 0}

for i in range(2, n + 1):
    D[i] = D[i - 1] + 1     # 1을 뺀다.
    
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)     # 2로 나눈다.
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)     # 3으로 나눈다.

print(D[n])
