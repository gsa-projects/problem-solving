import sys

problem_url = "https://boj.kr/1377"
problem_name = "버블 소트"
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

# O(1)에 알아내기 위해, 정렬할 때 값 순서로 해야 되니까 값을 앞에 배치
for i in range(n):
	A[i] = A[i], i

A.sort()

max_val = 0
for j in range(n):
	i = A[j][1]
	if max_val < i - j:
		max_val = i - j

print(max_val + 1)
