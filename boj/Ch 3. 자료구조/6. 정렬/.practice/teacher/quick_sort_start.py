def quick_sort(arr, s, e):
	if s < e:
		p = partition(arr, s, e)
		quick_sort(arr, s, p - 1)
		quick_sort(arr, p + 1, e)
		
def partition(arr, s, e):
	p = s
	left, right = s + 1, e
	
	while left <= right:
		while left <= right and arr[left] <= arr[p]:
			left += 1
		while left <= right and arr[right] >= arr[p]:
			right -= 1
		
		if left < right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
		
	arr[p], arr[right] = arr[right], arr[p]
	
	print(arr)
	
	return right

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
quick_sort(arr, 0, len(arr) - 1)
print('정렬 후: ', arr)
