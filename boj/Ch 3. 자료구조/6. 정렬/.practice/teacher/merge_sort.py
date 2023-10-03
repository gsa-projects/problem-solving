def merge_sort(arr, start, end):
	if start < end:
		mid = (start + end) // 2
		merge_sort(arr, start, mid)
		merge_sort(arr, mid + 1, end)
		merge(arr, start, mid, end)

result = 0

def merge(arr, start, mid, end):
	global result
	left_length = mid - start + 1
	right_length = end - (mid + 1) + 1
	
	# left = [arr[start + i] for i in range(left_length)]
	left = arr[start:mid + 1]
	# right = [arr[(mid + 1) + i] for i in range(right_length)]
	right = arr[mid + 1:end + 1]
	
	# merge
	i = j = 0   # left, right index
	k = start   # arr index
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
			result += (len(left) - i)   # todo: 백준 버블 소트
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
	
# arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = [10, 1, 5, 2, 3]
print('정렬 전  :', arr)
merge_sort(arr, 0, len(arr) - 1)
print('정렬 후  :', arr)
print(result)