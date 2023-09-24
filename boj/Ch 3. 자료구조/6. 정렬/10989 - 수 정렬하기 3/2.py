import sys
from collections import deque

# WC. PyPy3
#  - 메모리 초과
problem_url = "https://boj.kr/10989"
problem_name = "수 정렬하기 3"
input = sys.stdin.readline

n = int(input())
A = []

for _ in range(n):
	A.append(int(input()))

# WC. 메모리 초과
#  문제 조건에서 1 ≤ n ≤ 10,000,000 라서, 비둘기 집의 원리에 의해 적어도 한 버킷에 최소 1,000,000개의 요소가 들어감
#  - 버킷 개수를 늘려서 요소 개수를 줄인다
#  - 각 요소는 1 ≤ e ≤ 10,000 라서, 버킷을 10000개로 늘리면 최소 1000개

def radix_sort(A):
	exp = 1
	max_val = max(A)
	buckets = [deque() for _ in range(10000)]
	q = deque(A)
	
	while exp <= max_val:
		while q:
			val = q.popleft()
			idx = val - 1  # (val // exp) % 10
			buckets[idx].append(val)
		
		for bucket in buckets:
			while bucket:
				q.append(bucket.popleft())
		
		exp *= 10
	
	return list(q)

A = radix_sort(A)
for a in A:
	print(a)
