import sys
from heapq import heappush, heappop

# WC. PyPy3
#  - 시간 초과
#  - append가 임의의 인덱스의 값 변경보다 생각보다 훨씬 느림
problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
prior_q: list[tuple[int, int]] = []

answer = []

for i in range(n - 1, -1, -1):
	front = (i, heights[i])
	
	while prior_q and prior_q[0][1] <= front[1]:
		heappop(prior_q)
		answer.insert(0, front[0] + 1)
	
	heappush(prior_q, front)

while prior_q:
	heappop(prior_q)
	answer.insert(0, 0)

for e in answer:
	print(e, end=' ')
