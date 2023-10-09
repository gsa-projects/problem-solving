import sys

problem_url = "https://boj.kr/11441"
problem_name = "합 구하기"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())

C = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
	C[i] = C[i - 1] + A[i - 1]

for _ in range(q):
	x1, x2 = map(int, input().split())
	print(C[x2] - C[x1 - 1])
