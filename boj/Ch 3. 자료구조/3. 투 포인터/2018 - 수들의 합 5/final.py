import sys

problem_url = "https://boj.kr/2018"
problem_name = "수들의 합 5"
input = sys.stdin.readline

n = int(input())
A = list(range(1, n))

sum_range = lambda a, b: (a + b) * (b - a + 1) // 2
cnt = 1     # n 하나로 합이 n인 꼴 생략
l, r = 0, 1

while l <= r < len(A):
	s = sum_range(A[l], A[r])
	
	# 아래 코드에서 어쩌다 l == r을 만들어서 while 문이 예기치 않게 종료될 수 있을 것 같은데?
	#  while문을 l <= r로 수정했다. 물론 안해도 AC는 나오지만..
	if n > s:
		r += 1
	elif n < s:
		l += 1
	else:
		cnt += 1
		l += 1

print(cnt)
