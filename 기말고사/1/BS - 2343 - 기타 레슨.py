n, m = map(int, input().split())
T = list(map(int, input().split()))

# T.sort()
# note: 강의의 순서가 바뀌면 안된다고 문제에 명시되었음, 그리고 이 문제는 T에서 찾는 게 아니라서 정렬 ㄴㄴ

# note: 블루레이당 최소 capacity는 블루레이 1개당 강의가 1개씩 들어가는 N=M의 상황일 때 -> max(T)
#   - 블루레이당 최대 capacity는 블루레이 1개에 강의가 전부 들어가는 M=1의 상황일 때 -> sum(T)
left, right = max(T), sum(T)

def get_count_of_blueray(capacity):
    cnt = 1
    s = 0
    for i in range(len(T)):
        s += T[i]
        if s > capacity:
            cnt += 1
            s = T[i]

    return cnt

capacity = 0

while left <= right:
    mid = (left + right) // 2
    # 각 블루레이가 mid만큼의 capacity를 가질 때 몇 개의 블루레이가 필요한가를 구해서 그것을 m과 비교해야됨
    count = get_count_of_blueray(mid)

    # count == m 중 mid가 최소가 되게 하는 것을 찾아야 됨
    # count < m 라는 건 블루레이가 더 적게 필요하다, 즉 블루레이 당 capacity가 더 크다는 뜻
    # note: `count <= m` 이렇게 잡아야 이 if 문이 만족 안하는 경우는 count == m + 1 > m 일 때
    #    -> 블루레이 개수가 더 크므로 capacity가 더 작을 때. 즉, 마지막으로 만족하는 경우는 capacity가 최소일 경우
    if count <= m:
        capacity = mid
        right = mid - 1     # capacity를 줄인다 -> count를 늘린다
    else:   # m < count
        left = mid + 1      # capacity를 늘린다

print(capacity)
