import sys

# WC. PyPy3
#  - 시간 초과
#  - for 2중 루프가 문제인 듯
problem_url = "https://boj.kr/1377"
problem_name = "버블 소트"
input = sys.stdin.readline

# idea: 버블 소트할 때, 어떤 값이 1 iteration에 몇 번 오른쪽으로 밀리는지 알 수 있을까?
#  그건, 그 값이 겁나게 크다면 1 iteration에 끝까지도 쭈루룩 밀릴 수 있기 때문에 알 수 없다.
#  다만, 왼쪽으로는 진행하지 않으므로, 왼쪽으로 가는 것은 오직 다른 값에 의해 swap 된 경우 뿐이라, 최대 1번이다.

n = int(input())
A = [int(input()) for _ in range(n)]
A_sort = sorted(A)

max_count = 0
for i in range(n):
	for j in range(n):
		if A[i] == A_sort[j]:
			count = i - j + 1
			# print(i, j, count)
			
			if count > max_count:
				max_count = count

print(max_count)
