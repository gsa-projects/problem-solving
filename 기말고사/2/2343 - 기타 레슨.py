n, m = map(int, input().split())
T = list(map(int, input().split()))

# 주어진 게 블루레이의 개수이므로
# 함수 f는 역함수, 블루레이의 크기로부터 개수를 유도하는.
def f(x):
    cnt = 1     # note: 1부터 시작해야됨
    s = 0
    for i in range(n):
        if s + T[i] > x:
            cnt += 1
            s = 0
        s += T[i]
    return cnt

i, j = max(T), sum(T)
result = -1

while i <= j:
    mid = (i + j) // 2
    count = f(mid)

    # f와 mid의 증감은 반대 방향
    # mid의 최소를 구하라
    if count <= m:  # 부등호가 바뀌는 순간 -> count > m인 순간 -> mid < ~~ 인 순간 -> 최소
        result = mid
        j = mid - 1
    elif m < count:
        i = mid + 1

print(result)
