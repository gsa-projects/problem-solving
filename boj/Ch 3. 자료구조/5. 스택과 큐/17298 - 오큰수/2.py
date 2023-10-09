import sys
from collections import deque

# WC. PyPy3
#  - 시간 초과
problem_url = "https://boj.kr/17298"
problem_name = "오큰수"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dq = deque()
for i in range(1, n):
	# 어떤 수의 오큰수가 될 값의 인덱스는 전 값에 비해 더 큰 값인 경우의 인덱스
	# cuz 오큰수 정의가 오른쪽에 있는 수 중 나보다는 큰 수 중 가장 가까운 수
	if A[i - 1] < A[i]:
		dq.append(i)

# print(dq)

# WC. 반례
#  7
#  4 3 2 1 2 3 4
#  dq에 들어 있는게 다 오큰수가 되는 건 맞는데, dq.top 이 오큰수가 된다는 보장이 없다. 이 반례는 dq.tail 이 오큰수

NGE = []
for i in range(n):
	# 큐에 현재 인덱스 넘어가면 top 지우기
	if dq and i == dq[0]:
		dq.popleft()
	
	# 큐가 비어있으면 -1, 아니면 현재 값보다 top 인덱스의 값이 더 크면 그게 오큰수
	if not dq:
		NGE.append(-1)
	else:
		bl = False
		for q in dq:
			if A[i] < A[q]:
				NGE.append(A[q])
				bl = True
				break
		
		if not bl:
			NGE.append(-1)

for nge in NGE:
	print(nge, end=" ")
