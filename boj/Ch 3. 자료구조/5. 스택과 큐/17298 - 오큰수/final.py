import sys

problem_url = "https://boj.kr/17298"
problem_name = "오큰수"
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

S = []
NGE = [None] * n

for i in range(n):
	val = (i, A[i])
	
	while S and S[-1][1] < val[1]:
		NGE[S.pop()[0]] = val[1]
	
	S.append(val)

while S:
	NGE[S.pop()[0]] = -1

print(*NGE, sep=' ')
