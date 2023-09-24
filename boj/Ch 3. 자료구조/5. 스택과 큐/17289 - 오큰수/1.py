import sys
from collections import deque

# WC. PyPy3
#  - 틀렸습니다
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

NGE = []
for i in range(n):
	# 큐에 현재 인덱스 넘어가면 top 지우기
	if dq and i == dq[0]:
		dq.popleft()
	
	# 큐가 비어있으면 -1, 아니면 현재 값보다 top 인덱스의 값이 더 크면 그게 오큰수
	if not dq:
		NGE.append(-1)
	else:
		top = dq[0]
		if A[i] < A[top]:
			NGE.append(A[top])
		else:
			NGE.append(-1)

for nge in NGE:
	print(nge, end=" ")
