__problem__ = 'https://boj.kr/1463', '1로 만들기'

import sys
from math import inf

input = sys.stdin.readline

n = int(input())

D = [0] * (n + 1)

for i in range(2, n+1):
    D[i] = D[i - 1] + 1

    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)

print(D[n])
