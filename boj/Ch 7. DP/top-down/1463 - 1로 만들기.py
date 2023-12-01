__problem__ = 'https://boj.kr/1463', '1로 만들기'

import sys
from math import inf

input = sys.stdin.readline

n = int(input())

D = {1: 0}

# note: top-down은 재귀 호출 limit에 걸리게 되는데 setrecursionlimit를 늘리면 메모리가 늘어나서 메모리 초과
# def get(n):
#     if n not in D:
#         D[n] = get(n - 1) + 1
#
#         if n % 3 == 0:
#             D[n] = min(D[n], get(n // 3) + 1)
#         if n % 2 == 0:
#             D[n] = min(D[n], get(n // 2) + 1)
#
#     return D[n]
#
# print(get(n))
