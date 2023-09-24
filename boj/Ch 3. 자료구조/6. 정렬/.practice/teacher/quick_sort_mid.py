def quick_sort(arr, s, e):
	if s < e:
		p = partition(arr, s, e)
		quick_sort(arr, s, p - 1)
		quick_sort(arr, p, e)

def partition(arr, s, e):
	p = arr[(s + e) // 2]
	left, right = s, e
	
	print(arr[s:e + 1], 'pivot:', p)
	
	while left <= right:
		while arr[left] < p:
			left += 1
		while arr[right] > p:
			right -= 1
		
		if left <= right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
	
	print(arr[s:e+1])
	
	return left

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
quick_sort(arr, 0, len(arr) - 1)
print('정렬 후: ', arr)
