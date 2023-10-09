import sys

problem_url = "https://boj.kr/10986"
problem_name = "나머지 합"
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * n
C[0] = A[0]
for i in range(1, n):
	C[i] = C[i - 1] + A[i]

cnt = 0
F = [0] * m
for c in C:
	rem = c % m
	if rem == 0:
		cnt += 1
	F[rem] += 1

for f in F:
	if f > 1:
		cnt += f * (f - 1) // 2

print(cnt)
