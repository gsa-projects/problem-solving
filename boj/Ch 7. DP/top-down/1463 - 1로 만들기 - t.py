__problem__ = 'https://boj.kr/1463', '1로 만들기'

import sys
from math import inf

input = sys.stdin.readline

n = int(input())

D = {1: 0}

def get(n):
    if n in D:
        return D[n]
    if n % 6 == 0:
        D[n] = min(get(n // 3), get(n // 2)) + 1
    elif n % 3 == 0:
        D[n] = min(get(n // 3), get(n - 1)) + 1
    elif n % 2 == 0:
        D[n] = min(get(n // 2), get(n - 1)) + 1
    else:
        D[n] = get(n - 1) + 1

    return D[n]

print(get(n))
