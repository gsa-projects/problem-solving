def insertion_sort(arr):
	for i in range(1, len(arr)):
		
		# todo: while로?
		for j in range(i - 1, -1, -1):
			if arr[j] > arr[j + 1]:     # 이미 S는 모두 정렬되었기 때문에 이 조건문이 만족되는 것 자체가 걍 arr[j+1]가 방금 들어온 값이라는거임
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		print(arr)
	
	

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
insertion_sort(arr)
print('정렬 후: ', arr)
