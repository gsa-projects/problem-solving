from kit import sort_test

def merge_sort(arr, start=0, end=None):
	if end is None:
		end = len(arr) - 1
	
	if start < end:
		mid = (start + end) // 2
		merge_sort(arr, start, mid)
		merge_sort(arr, mid + 1, end)
		merge(arr, start, mid, end)
	
	return arr

def merge(arr, start, mid, end):
	global result
	left_length = mid - start + 1
	right_length = end - (mid + 1) + 1
	
	# left = [arr[start + i] for i in range(left_length)]
	left = arr[start:mid + 1]
	# right = [arr[(mid + 1) + i] for i in range(right_length)]
	right = arr[mid + 1:end + 1]
	
	# merge
	i = j = 0  # left, right index
	k = start  # arr index
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	
	# 남은 리스트 요소를 배열에 추가 처리
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1

sort_test(merge_sort)
