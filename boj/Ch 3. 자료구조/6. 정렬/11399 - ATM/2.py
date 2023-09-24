import sys

# AC. PyPy3
#  - for 문 내부를 while 문으로 대체한 내 코드, 128ms
problem_url = "https://boj.kr/11399"
problem_name = "ATM"
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

# 삽입 정렬
for i in range(1, n):
	j = i - 1
	while j >= 0:
		if times[j] > times[j + 1]:
			times[j], times[j + 1] = times[j + 1], times[j]
		
		j -= 1

cum = [0 for _ in range(n)]
for i in range(n):
	cum[i] = (0 if i == 0 else cum[i - 1]) + times[i]

print(sum(cum))
