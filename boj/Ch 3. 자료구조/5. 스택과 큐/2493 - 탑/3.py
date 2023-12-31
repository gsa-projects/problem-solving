import sys
from heapq import heappush, heappop

# AC. PyPy3
#  - 우선순위 큐를 사용해봄
problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
prior_q: list[tuple[int, int]] = []

answer = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
	front = (i, heights[i])
	
	while prior_q and prior_q[0][1] <= front[1]:
		idx, height = heappop(prior_q)
		answer[idx] = front[0] + 1
	
	heappush(prior_q, front)

for e in answer:
	print(e, end=' ')
