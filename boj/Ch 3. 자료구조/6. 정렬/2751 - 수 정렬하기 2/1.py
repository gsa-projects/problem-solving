import sys

# WC. PyPy3
#  - 런타임 에러 (RecursionError)
#  - teacherlize한 내 코드
problem_url = "https://boj.kr/2751"
problem_name = "수 정렬하기 2"
input = sys.stdin.readline

n = int(input())
A = []

for _ in range(n):
	A.append(int(input()))

def quick_sort(A, s, e):
	if s < e:
		pivot = partition(A, s, e)
		quick_sort(A, s, pivot - 1)
		quick_sort(A, pivot + 1, e)

def partition(A, s, e) -> int:
	pivot = s
	left, right = s + 1, e
	
	while left <= right:
		while left <= right and A[left] <= A[pivot]:
			left += 1
		
		while left <= right and A[pivot] <= A[right]:
			right -= 1
		
		if left < right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
	
	A[pivot], A[right] = A[right], A[pivot]
	
	return right

quick_sort(A, 0, n - 1)
for a in A:
	print(a)
