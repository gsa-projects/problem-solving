import sys

problem_url = "https://boj.kr/10989"
problem_name = "수 정렬하기 3"
input = sys.stdin.readline

n = int(input())
F = [0 for _ in range(10000)]

for _ in range(n):
	query = int(input())
	F[query - 1] += 1

for i in range(len(F)):
	for _ in range(F[i]):
		print(i + 1)
