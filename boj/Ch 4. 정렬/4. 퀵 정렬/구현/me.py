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
	
	@staticmethod
	def front_partition(arr, s, e):
		p = s
		l, r = s + 1, e
		
		while l <= r:
			while l <= r and arr[l] <= arr[p]:
				l += 1
			
			while l <= r and arr[p] <= arr[r]:
				r -= 1
				
			if l < r:
				arr[l], arr[r] = arr[r], arr[l]
				l += 1
				r -= 1
		
		arr[p], arr[r] = arr[r], arr[p]
		p, r = r, p
		
		return p
	
	@staticmethod
	def back(arr, s=0, e=None):
		if e is None:
			e = len(arr) - 1
		
		if s < e:
			p = quick_sort.back_partition(arr, s, e)
			quick_sort.back(arr, s, p - 1)
			quick_sort.back(arr, p + 1, e)
	
	@staticmethod
	def back_partition(arr, s, e):
		p = e
		l, r = s, e - 1
	
	@staticmethod
	def middle(arr, s=0, e=None):
		...
	
	@staticmethod
	def middle_partition(arr, s, e):
		...

sort_test(quick_sort.front)
# sort_test(quick_sort.middle)
# sort_test(quick_sort.back)
