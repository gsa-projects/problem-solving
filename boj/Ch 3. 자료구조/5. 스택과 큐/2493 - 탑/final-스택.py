import sys

problem_url = "https://boj.kr/2493"
problem_name = "탑"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
S = []
R = [0] * n

for i in range(n):
	val = (i, A[i])
	
	while S and S[-1][1] < val[1]:
		S.pop()
	
	if S:
		R[i] = S[-1][0] + 1
	
	S.append(val)

print(*R)
