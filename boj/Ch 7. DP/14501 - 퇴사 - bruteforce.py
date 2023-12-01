__problem__ = 'https://boj.kr/14501', '퇴사'

import sys

input = sys.stdin.readline

N = int(input())
T = [0] * N
P = [0] * N
ans = 0

for i in range(N):
    T[i], P[i] = map(int, input().split())

def dfs(n, cost):
    global ans

    if n >= N:
        ans = max(ans, cost)
        return

    if n + T[n] <= N:
        dfs(n + T[n], cost + P[n])  # 상담이 가능한 경우
    else:
        dfs(n + 1, cost)    # 상담이 가능하지 않은 경우

dfs(0, 0)
print(ans)
