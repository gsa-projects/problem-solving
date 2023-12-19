from heapq import heappush, heappop

n = int(input())
A = []
for _ in range(n):
    heappush(A, int(input()))

s = 0
while len(A) >= 2:
    t = heappop(A) + heappop(A)
    s += t
    heappush(A, t)

print(s)
