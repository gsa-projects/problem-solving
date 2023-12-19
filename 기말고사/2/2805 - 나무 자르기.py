n, m = map(int, input().split())
H = list(map(int, input().split()))

# M 미터의 나무를 가져갈 수 있는 높이의 최댓값을 찾고 싶다.
# 역함수, 높이로부터 미터를 구하는 함수 f
def f(x):
    return sum(max(0, H[i] - x) for i in range(n))

i, j = 0, max(H)
result = -1

while i <= j:
    mid = (i + j) // 2
    count = f(mid)

    # f(x)와 x의 방향은 반대 방향
    # 높이의 최댓값 -> 개수의 최소
    if count < m:   # 부등호 바꿨을 때 일어날 일 (증감의 결과)
        j = mid - 1
    elif count >= m:
        result = mid
        i = mid + 1

print(result)
