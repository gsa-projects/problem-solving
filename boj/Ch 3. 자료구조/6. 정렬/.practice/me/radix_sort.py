from collections import deque

def radix_sort(arr):
	buckets = [deque() for _ in range(10)]
	queue = deque(arr)
	max_val = max(arr)
	exp = 1
	
	while exp <= max_val:
		while queue:
			val = queue.popleft()
			mod = (val // exp) % 10
			buckets[mod].append(val)
		
		for bucket in buckets:
			while bucket:
				queue.append(bucket.popleft())
		
		exp *= 10
	
	return list(queue)

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print('정렬 전  :', arr)
arr = radix_sort(arr)
print('정렬 후  :', arr)