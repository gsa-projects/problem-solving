import sys

problem_url = "https://boj.kr/17298"
problem_name = "오큰수"
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
stack = [numbers[0]]

for i in range(n):
	if i + 1 < n:
		stack.append(numbers[i + 1])
	print(stack[-1], end=' '1)
	
	# numbers = [3, 5, 2, 7]
	# 스택에 넣을 때 top보다 더 큰 걸 넣으면 기존 거 팝
