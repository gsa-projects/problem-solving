import sys

problem_url = "https://boj.kr/10986"
problem_name = "나머지 합"
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

C = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
	C[i] = (C[i - 1] + A[i - 1]) % m
del C[0]

F = [0 for _ in range(m)]
for c in C:
	F[c] += 1

cnt = 0
for f in F:
	cnt += f * (f - 1) // 2
cnt += F[0]

print(cnt)
