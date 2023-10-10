from kit import sort_test

def insertion_sort(A):
	for i in range(len(A)):
		e = A[i]
		j = i - 1
		while j >= 0 and A[j] > e:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = e

sort_test(insertion_sort)
