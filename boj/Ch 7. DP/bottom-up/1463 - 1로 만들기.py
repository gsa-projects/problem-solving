__problem__ = 'https://boj.kr/1463', '1로 만들기'

import sys
from math import inf

input = sys.stdin.readline

n = int(input())

# 10 -> 9 -> 3 -> 1 로 하는 것이 제일 빠르기 때문에, 즉 1을 먼저 빼는게 더 빠른 경우가 있어서 그리디로는 풀 수 없음
D = [0] * (n + 1)

for i in range(2, n+1):
    min_way = inf

    if i % 3 == 0:
        min_way = min(min_way, D[i // 3] + 1)
    if i % 2 == 0:
        min_way = min(min_way, D[i // 2] + 1)
    min_way = min(min_way, D[i - 1] + 1)

    D[i] = min_way

print(D[n])
