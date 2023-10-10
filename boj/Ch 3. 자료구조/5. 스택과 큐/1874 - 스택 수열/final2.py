import sys

input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]
S = []
ans = []
i = 1
for query in A:
	if not S or query >= i:
		while not S or query >= i:
			S.append(i)
			ans.append('+')
			i += 1
		S.pop()
		ans.append('-')
	else:
		val = S.pop()
		if val < query:
			print('NO')
			exit()
		else:
			ans.append('-')

print(*ans, sep='\n')
