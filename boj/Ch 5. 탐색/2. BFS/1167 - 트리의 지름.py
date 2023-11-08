__problem__ = 'https://boj.kr/1167', '트리의 지름'

import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
vertices = [[] for _ in range(v + 1)]
# note: 내가 볼 때 [0, v) 가 아니고 [1, v]라서 v+1를 해주는 것에서 시험 실수 개많이 할 듯

for _ in range(v):
    inp = list(map(int, input().split()))

    idx = inp[0]
    for i in range(1, len(inp) - 1, 2):     # 마지막 값은 -1이니까 제외
        vertices[idx].append((inp[i], inp[i + 1]))      # (정점 번호, 정점까지의 거리)

