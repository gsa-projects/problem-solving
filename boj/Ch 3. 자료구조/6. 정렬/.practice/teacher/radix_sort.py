from collections import deque

# todo: 이건 '기수' 정렬으로, 10진수는 각 자릿수가 0~9라는 것을 이용해서 버킷을 10개 만들었는데,
#  백준에서는 '계수' 정렬을 필요로 하고, 이는 모든 수가 1만 미만이므로 버킷을 1만개 만들어버리는 방법
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

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print('정렬 전  :', arr)
arr = radix_sort(arr)
print('정렬 후  :', arr)