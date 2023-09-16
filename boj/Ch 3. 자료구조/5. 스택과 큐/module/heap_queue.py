from heapq import heappush, heappop

A = [3, 2, 1, -1, -2, -3]
q = []

for a in A:
	heappush(q, (abs(a), a))
	
for _ in range(len(q)):
	print(heappop(q))