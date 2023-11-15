__problem__ = 'https://boj.kr/1167', '트리의 지름'
# 트리이기 때문에 끊어진 그래프는 없음, 연결요소 1개

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
# note: 내가 볼 때 정점 번호가 1부터 시작( [0, n) 가 아니고 [1, n+1] )해서 n+1를 해주는 것에서 시험 실수 개많이 할 듯

for _ in range(n):
    inp = list(map(int, input().split()))

    idx = inp[0]
    for i in range(1, len(inp) - 1, 2):     # 마지막 값은 -1이니까 제외
        # 거리는 모두 양수
        graph[idx].append((inp[i], inp[i + 1]))      # (정점 번호, 정점까지의 거리)

def bfs(g, s: int) -> list[int]:
    distance = [-1] * (n + 1)   # 0으로 초기화해도 되긴 하는데 -1로 초기화하면 처음 정점 위치만 0이라 처음 정점 위치도 알 수 있음
    # distance[i] = s부터 i번 정점까지의 거리, distance[i] < 0으로 visit했는지 확인하는 효과까지 덤으로

    q = deque([(s, 0)])

    while q:
        v, dist_to_v = q.popleft()
        distance[v] = dist_to_v

        for w, d in g[v]:
            if distance[w] < 0:
                q.append((w, dist_to_v + d))

    return distance

# todo: 사실 이거 왜 이렇게 하면 지름 되는지 이해 못함
distance_from_1 = bfs(graph, 1)
idxmax = distance_from_1.index(max(distance_from_1))
print(max(bfs(graph, idxmax)))
