from kit import sort_test

class quick_sort:
	@staticmethod
	def front(arr, s=0, e=None):
		if e is None:
			e = len(arr) - 1
		
		if s < e:
			p = quick_sort.front_partition(arr, s, e)
			quick_sort.front(arr, s, p - 1)
			quick_sort.front(arr, p + 1, e)
		
		return arr
	
	@staticmethod
	def front_partition(arr, s, e):
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
		
		# print(arr)
		
		return right
	
	@staticmethod
	def back(arr, start=0, end=None):
		if end is None:
			end = len(arr) - 1
		
		if start >= end:
			return
		pivot = end
		left, right = start, end - 1
		
		while left <= right:
			while left <= right and arr[left] <= arr[pivot]:
				left += 1
			while left <= right and arr[right] >= arr[pivot]:
				right -= 1
			if left < right:
				arr[left], arr[right] = arr[right], arr[left]
				left += 1
				right -= 1
		arr[left], arr[pivot] = arr[pivot], arr[left]
		
		quick_sort.back(arr, start, left - 1)
		quick_sort.back(arr, left + 1, end)
		
		return arr
	
	@staticmethod
	def middle(arr, s=0, e=None):
		if e is None:
			e = len(arr) - 1
		
		if s < e:
			p = quick_sort.middle_partition(arr, s, e)
			quick_sort.middle(arr, s, p - 1)
			quick_sort.middle(arr, p, e)
			
		return arr
	
	@staticmethod
	def middle_partition(arr, s, e):
		p = arr[(s + e) // 2]
		left, right = s, e
		
		# print(arr[s:e + 1], 'pivot:', p)
		
		while left <= right:
			while arr[left] < p:
				left += 1
			while arr[right] > p:
				right -= 1
			
			if left <= right:
				arr[left], arr[right] = arr[right], arr[left]
				left += 1
				right -= 1
		
		# print(arr[s:e + 1])
		
		return left

sort_test(quick_sort.middle)
