# note: 어느 범위에서 어떤 값을 얻는가?
#   - 블루레이의 크기를 찾아내는 것. 블루레이의 크기는 리스트에서 찾는 것이 아니고 그냥 정수 전체에서 찾음

n, m = map(int, input().split())
T = list(map(int, input().split()))

# note: 블루레이의 크기는 어떤 범위를 갖는가?
#   - 블루레이의 개수는 m. 1 <= m <= n 이라는 조건이 문제에서 주어진다.
#   - 최소: m = n일 때 블루레이에는 단 1개씩의 강의만 들어간다. -> max(T)
#   - 최대: m = 1일 때 블루레이에는 모든 강의가 들어간다. -> sum(T)

left, right = max(T), sum(T)

# note: 블루레이의 크기는 어떻게 찾는가?
#   - 블루레이의 개수 m은 주어졌으므로, 임의의 블루레이의 크기로부터 개수를 얻어내어 이 값을 m과 비교하며 이진탐색

def get_count_from_capacity(capacity):
    count = 1
    s = 0
    for i in range(len(T)):
        if s + T[i] > capacity:
            count += 1
            s = 0
        s += T[i]

    return count

result = -1

while left <= right:
    mid = (left + right) // 2   # mid의 크기를 갖는 블루레이로는 T를 몇 개로 채울 수 있을까?
    count = get_count_from_capacity(mid)

    # note: 최소 크기를 구하려면 어떻게 이진 탐색을 해야할까?
    #   - 우리는 조건문에서 개수인 m과 count를 비교해야 한다.
    #   - 개수가 크다 -> 크기가 작다
    #   - 개수가 오버해서 커지는 경우를 등호를 붙이지 않으면 된다

    if m < count:   # 개수를 오버함 -> 크기가 너무 작음
        left = mid + 1
    else:   # count <= m. 개수가 적거나 같음 -> 크기가 같거나 큼 -> 점점 크기를 작게 조정할 것임
        result = mid
        right = mid - 1

print(result)
