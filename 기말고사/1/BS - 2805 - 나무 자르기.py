n, m = map(int, input().split())
H = list(map(int, input().split()))

# 이분탐색: f(h) = m 이 되도록. f는 높이로부터 개수를 구하는 함수
def f(h):
    return sum(max(0, e - h) for e in H)

i, j = 0, max(H)
result = -1

while i <= j:
    k = (i + j) // 2
    cnt = f(k)

    # 높이가 최대가 되도록 -> k가 최대가 되도록 -> cnt가 최소 (m == cnt긴 하지만 아무튼)
    if cnt < m:
        # 나무가 너무 적게 잘리면 높이를 내려
        j = k - 1
    elif m <= cnt:
        result = k
        i = k + 1

print(result)
