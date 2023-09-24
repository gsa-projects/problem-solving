# def quick_sort(arr, start, end):
# 	if start < end:
# 		pivot = partition(arr, start, end)
# 		quick_sort(arr, start, pivot - 1)
# 		quick_sort(arr, pivot + 1, end)
#
# def partition(arr, start, end):
# 	pivot = start
# 	left, right = start + 1, end
#
# 	while left <= right:
# 		while left <= right and arr[left] <= arr[pivot]:
# 			left += 1
#
# 		while left <= right and arr[pivot] <= arr[right]:
# 			right -= 1
#
# 		if left < right:    # and arr[left] >= arr[pivot] >= arr[right]: idea: 이거 항상 만족함 위에 while 구문 다 돌았으면
# 			arr[left], arr[right] = arr[right], arr[left]
# 			left += 1
# 			right -= 1
#
# 	arr[pivot], arr[right] = arr[right], arr[pivot]
#
# 	return right

def quick_sort(arr, start, end):
	if start >= end:
		return
	
	pivot = start
	left, right = start + 1, end
	
	while left <= right:
		while left <= right and arr[left] <= arr[pivot]:
			left += 1
		
		while left <= right and arr[pivot] <= arr[right]:
			right -= 1
		
		if left < right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
	
	arr[right], arr[pivot] = arr[pivot], arr[right]
	
	quick_sort(arr, start, right - 1)
	quick_sort(arr, right + 1, end)

arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print('정렬 전: ', arr)
quick_sort(arr, 0, len(arr) - 1)
print('정렬 후: ', arr)