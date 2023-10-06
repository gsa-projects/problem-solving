from kit import sort_test
from collections import deque

def radix_sort(arr):
	buckets = [deque() for _ in range(10)]
	queue = deque(arr)
	
	exp = 1
	max_value = max(arr)
	
	while exp <= max_value:
		while queue:
			num = queue.popleft()
			i = (num // exp) % 10
			buckets[i].append(num)
		
		for bucket in buckets:
			while bucket:
				queue.append(bucket.popleft())
		
		exp *= 10
	
	return list(queue)

sort_test(radix_sort)
