def merge_sort(arr, start, end):
	if start < end:
		mid = (start + end) // 2
		merge_sort(arr, start, mid)
		merge_sort(arr, mid + 1, end)
		merge(arr, start, mid, end)

def merge(arr, start, mid, end):
	left = arr[start:mid+1]
	right = arr[mid+1:end+1]
	
	i, j = 0, 0
	k = start
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	
	# left 전체가 right 보다 작은 경우, 위의 while 구문은 j = 0, i = len(left) 상태로 끝날 수도 있다.
	# 반대의 경우인 j = len(right), i = 0 의 경우도 가능
	# 따라서 아래의 두 개의 while 구문은 항상 최대 1개만 실행된다.
	
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
		
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전  :', arr)
merge_sort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)