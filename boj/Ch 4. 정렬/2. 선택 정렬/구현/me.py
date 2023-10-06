from kit import sort_test

def selection_sort(arr):
	for i in range(len(arr) - 1):
		min_idx = i
		for j in range(i, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		
		arr[min_idx], arr[i] = arr[i], arr[min_idx]
		
	return arr

sort_test(selection_sort)
