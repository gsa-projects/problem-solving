from kit import sort_test

def merge_sort(A, s, e):
	if s < e:
		mid = (s + e) // 2
		merge_sort(A, s, mid)
		merge_sort(A, mid + 1, e)
		merge(A, s, mid, e)
	
	return A

def merge(A, s, m, e):
	L = A[s:m + 1]
	R = A[m + 1:e + 1]

	n_l = len(L)
	n_r = len(R)
	# -----------
	# n_l = m - s + 1
	# n_r = e - m
	#
	# L = [A[s + i] for i in range(n_l)]
	# R = [A[m + 1 + i] for i in range(n_r)]
	
	l, r = 0, 0
	i = s
	
	while l < n_l and r < n_r:
		if L[l] <= R[r]:    # note. 등호 필수 !!!!!!!!!!!!!!!!!!!!!!!!! 이래야 안정 정렬이 성립함.
			A[i] = L[l]
			l += 1
		else:
			A[i] = R[r]
			r += 1
		i += 1
	
	while l < n_l:
		A[i] = L[l]
		i += 1
		l += 1
	
	while r < n_r:
		A[i] = R[r]
		i += 1
		r += 1
		
sort_test(merge_sort)
