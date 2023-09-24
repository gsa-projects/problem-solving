import sys

# WC. PyPy3
#  - 런타임 에러 (NZEC), exit code가 0이 아닐 때 발생하는 에러
problem_name = "스택 수열"
problem_url = "https://boj.kr/1874"
input = sys.stdin.readline

stack = []
way = []

n = int(input())
keys = []
for _ in range(n):
	keys.append(int(input()))

i = 1
for key in keys:
	while True:
		if ((not stack) or stack[-1] < key) and i <= n:
			stack.append(i)
			i += 1
			way.append('+')
		
		if stack and stack[-1] > key:
			print('NO')
			exit(1)
		
		if stack and stack[-1] == key:
			stack.pop()
			way.append('-')
			break

for e in way:
	print(e)
