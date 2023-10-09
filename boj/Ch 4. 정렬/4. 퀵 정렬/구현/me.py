from kit import sort_test

class quick_sort:
	@staticmethod
	def front(A, s, e):
		if s < e:
			p = quick_sort.front_partition(A, s, e)
			quick_sort.front(A, s, p - 1)
			quick_sort.front(A, p + 1, e)
	
	@staticmethod
	def front_partition(A, s, e):
		p = s
		l, r = s + 1, e
		
		while l <= r:
			while l <= r and A[l] <= A[p]:
				l += 1
			
			while l <= r and A[p] <= A[r]:
				r -= 1
				
			if l < r:
				A[l], A[r] = A[r], A[l]
				l += 1
				r -= 1
		
		A[p], A[r] = A[r], A[p]
		p, r = r, p
		
		return p
	
	@staticmethod
	def back(A, s, e):
		if s < e:
			p = quick_sort.back_partition(A, s, e)
			quick_sort.back(A, s, p - 1)
			quick_sort.back(A, p + 1, e)
	
	@staticmethod
	def back_partition(A, s, e):
		p = e
		l, r = s, e - 1
		
		while l <= r:
			while l <= r and A[l] <= A[p]:
				l += 1
			
			while l <= r and A[p] <= A[r]:
				r -= 1
			
			if l < r:
				A[l], A[r] = A[r], A[l]
				l += 1
				r -= 1
		
		A[l], A[p] = A[p], A[l]
		l, p = p, l
		
		return p
	
	@staticmethod
	def middle(A, s, e):
		if s < e:
			p = quick_sort.middle_partition(A, s, e)
			
			quick_sort.middle(A, s, p - 1)
			quick_sort.middle(A, p, e)
			# p-1, p로 경계 조건을 잡았다는 것은, partition에서 l을 반환하겠다는 다짐 -> 근데 r로 반환 하는건 안됨 경계 조건 바꿔도
	
	@staticmethod
	def middle_partition(A, s, e):
		p = A[(s + e) // 2]
		l, r = s, e
		
		while l <= r:
			# 위의 두 while 문의 l <= r은 생략 가능
			while l <= r and A[l] < p:
				l += 1
			while l <= r and p < A[r]:
				r -= 1
			if l <= r:
				A[l], A[r] = A[r], A[l]
				l += 1
				r -= 1
		
		return l
		

sort_test(quick_sort.front)
sort_test(quick_sort.middle)
sort_test(quick_sort.back)
