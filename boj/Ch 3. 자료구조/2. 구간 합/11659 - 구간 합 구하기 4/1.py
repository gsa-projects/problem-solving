import sys

# AC. Python 3
problem_url = "https://boj.kr/11659"
problem_name = "구간 합 구하기 4"
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cum_arr = [arr[0]]
for i in range(1, len(arr)):
	cum_arr.append(cum_arr[i - 1] + arr[i])

for _ in range(m):
	i, j = map(lambda x: int(x) - 1, input().split())
	
	print(cum_arr[j] - (0 if i - 1 == -1 else cum_arr[i - 1]))
