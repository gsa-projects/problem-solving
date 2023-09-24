def bubble_sort(arr: list[int, ...]):
	for i in range(1, len(arr)):
		for j in range(len(arr) - i):   # [0, n-1)
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		print(f'step {i:02d} : {arr}')

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
bubble_sort(arr)
print('정렬 후: ', arr)
