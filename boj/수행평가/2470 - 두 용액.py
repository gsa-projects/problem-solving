__problem__ = 'https://boj.kr/2470', '두 용액'

import sys

input = sys.stdin.readline

n = int(input())
V = list(map(int, input().split()))

V.sort()

i, j = 0, n - 1
min_i, min_j = i, j
min_v = abs(V[min_i] + V[min_j])

while i < j:
    s = V[i] + V[j]

    if min_v > abs(s):
        min_i, min_j = i, j
        min_v = abs(s)

    if s > 0:
        j -= 1
    elif s < 0:
        i += 1
    else:
        break

print(V[min_i], V[min_j])
