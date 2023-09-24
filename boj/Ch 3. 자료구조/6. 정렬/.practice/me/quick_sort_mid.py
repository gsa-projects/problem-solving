# todo: 어떻게 할까요

def quick_sort(arr, start, end):
	if start < end:
		pivot = partition(arr, start, end)
		quick_sort(arr, start, pivot - 1)
		quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
	pivot = start
	left, right = start + 1, end
	
	while left <= right:
		while left <= right and arr[left] <= arr[pivot]:
			left += 1
		
		while left <= right and arr[pivot] <= arr[right]:
			right -= 1
		
		if left < right:    # and arr[left] >= arr[pivot] >= arr[right]: idea: 이거 항상 만족함 위에 while 구문 다 돌았으면
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
	
	arr[pivot], arr[right] = arr[right], arr[pivot]
	
	return right


arr = [100, 5, 16, 3, 11, 53, 75, 61, 9]
print('정렬 전: ', arr)
quick_sort(arr, 0, len(arr))
print('정렬 후: ', arr)