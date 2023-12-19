N = int(input())
T = [0] * N
P = [0] * N
D = [0] * (N + 1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        # note: if 문이 헷갈리지 않음. 시간을 넘기지 않는다는 조건은 D의 IndexError를 막기 위함과 동치임
        D[i] = max(D[i + 1], D[i + T[i]] + P[i])
    else:
        D[i] = D[i + 1]

print(D[0])
