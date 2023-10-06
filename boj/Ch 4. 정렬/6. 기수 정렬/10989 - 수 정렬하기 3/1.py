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

def radix_sort(A):
	exp = 1
	max_val = max(A)
	buckets = [deque() for _ in range(10)]
	q = deque(A)
	
	while exp <= max_val:
		while q:
			val = q.popleft()
			idx = (val // exp) % 10
			buckets[idx].append(val)
		
		for bucket in buckets:
			while bucket:
				q.append(bucket.popleft())
		
		exp *= 10
	
	return list(q)

A = radix_sort(A)
for a in A:
	print(a)