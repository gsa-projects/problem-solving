def selection_sort(arr):
	for i in range(len(arr) - 1):
		min_idx = i
		
		for j in range(i + 1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		
		print(f'step {i+1:02d} : {arr}')
		
arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
selection_sort(arr)
print('정렬 후: ', arr)
