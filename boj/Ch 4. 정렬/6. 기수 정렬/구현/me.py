from kit import sort_test
from collections import deque

def radix_sort(arr):
	buckets = [deque() for _ in range(10)]
	q = deque(arr)
	
	if not q:
		return arr
	
	exp = 1
	max_num = max(arr)
	
	while exp <= max_num:
		while q:
			val = q.popleft()
			idx = (val // exp) % 10
			buckets[idx].append(val)    # push 아님!!!!!!
		
		for bucket in buckets:
			while bucket:
				q.append(bucket.popleft())
		
		exp *= 10
	
	return list(q)

sort_test(radix_sort)
