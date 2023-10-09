import sys
from heapq import heappush, heappop

problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
P = []
R = [0] * n

for i in range(n - 1, -1, -1):
	val = (i, A[i])
	
	while P and P[0][1] < val[1]:
		R[heappop(P)[0]] = val[0] + 1
	
	heappush(P, val)

print(*R)
