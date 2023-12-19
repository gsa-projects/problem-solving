n = int(input())
k = int(input())

# B[k]를 얻고 싶다
# 역함수 개념으로, B[k]로부터 k를 얻는 함수
def f(x):
    # n = 3, B[k] = 6
    # [1 2 3]
    # [2 4 6]
    # [3 6] 9
    # -> [1 2 2 3 3 4 6 6] 9
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, x // i)   # note: max라고 했었음
    return cnt

i, j = 0, k     # B[k] <= k 이기 때문
result = -1

while i <= j:
    mid = (i + j) // 2
    k_maybe = f(mid)

    # f(k)와 k의 방향성 동일
    # f(k)는 사실 k가 아니라 (k의 후보 중 가장 큰 애 + 1)을 반환함 -> f(k) > k -> f(k)의 최솟값을 찾아라
    if k_maybe < k:
        i = mid + 1
    elif k <= k_maybe:
        result = mid
        j = mid - 1

print(result)
