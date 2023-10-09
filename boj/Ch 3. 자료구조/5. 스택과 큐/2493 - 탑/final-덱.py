import sys
from collections import deque

problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
Q = deque()
R = [0] * n

for i in range(n - 1, -1, -1):
	val = (i, A[i])
	
	while Q and Q[-1][1] < val[1]:
		R[Q.pop()[0]] = val[0] + 1
	
	Q.append(val)

print(*R)
