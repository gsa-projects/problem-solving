import sys

# AC. 누적 합보단 슬라이딩 윈도우 문제가 맞는 것 같은데?
problem_url = "https://boj.kr/2559"
problem_name = "수열"
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

# 1 2 3  4  5
# 1 3 6  9 12
C = [0 for _ in range(n - k + 1)]
C[0] = sum(A[:k])

for i in range(1, len(C)):
	C[i] = C[i - 1] + A[k + i - 1] - A[i - 1]

print(max(C))
