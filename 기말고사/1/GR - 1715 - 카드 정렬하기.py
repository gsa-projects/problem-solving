from heapq import heappush, heappop

n = int(input())
# A = [int(input()) for _ in range(n)]
# note: heap으로 사용하려면 아예 빈 리스트에서부터 삽입을 heappush로 해야됨
A = []
for _ in range(n):
    heappush(A, int(input()))

# (20, 30), 30, 40
# 50, 30, 40 -> (30, 40), 50
# 70, 50 -> (50, 70)
# 120
# 계속 A에서 최솟값 2개들을 더하고 다시 푸시하고 더하고 반복 -> 정렬을 매 번하면 힘드므로 heappop 사용

sum = 0
while len(A) >= 2:
    x = heappop(A) + heappop(A)
    sum += x
    heappush(A, x)

print(sum)
