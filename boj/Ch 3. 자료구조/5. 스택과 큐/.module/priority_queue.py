from queue import PriorityQueue

A = [3, 2, 1, -1, -2, -3]
q = PriorityQueue()

for a in A:
	q.put((abs(a), a))
	
for _ in range(q.qsize()):
	print(q.get())