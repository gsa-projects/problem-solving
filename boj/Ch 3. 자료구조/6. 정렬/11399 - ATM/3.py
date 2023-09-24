import sys

# AC. PyPy3
#  - 쌤 코드, 116ms
problem_url = "https://boj.kr/11399"
problem_name = "ATM"
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

# 삽입 정렬
for i in range(n):
	j = i - 1
	key = times[i]
	
	while j >= 0 and times[j] > key:
		times[j + 1] = times[j]
		j -= 1
	times[j + 1] = key

cum = [0 for _ in range(n)]
for i in range(n):
	cum[i] = (0 if i == 0 else cum[i - 1]) + times[i]

print(sum(cum))
