import sys
from heapq import heappush, heappop

# AC. PyPy3
#  - 큐 요소 데이터 구조가 (인덱스, 값) 이 아니라 (값, 인덱스) 여도 됨
#  - 인덱스가 큰데 값(높이)도 큰 경우는 이미 pop를 다 당해서 남는 건 인덱스와 값이 동시에 작은 경우만 남음
problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
prior_q: list[tuple[int, int]] = []

answer = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
	front = (heights[i], i)
	
	while prior_q and prior_q[0][0] <= front[0]:
		height, idx = heappop(prior_q)
		answer[idx] = front[1] + 1
	
	heappush(prior_q, front)

for e in answer:
	print(e, end=' ')
