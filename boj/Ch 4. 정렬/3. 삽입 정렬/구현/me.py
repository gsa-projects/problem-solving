from kit import sort_test
from random import shuffle

case = list(range(1, 10))
shuffle(case)

def insertion_sort(arr):
	for i in range(1, len(arr)):
		e = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > e:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = e

	return arr

def insertion_sort_2(arr):
	for i in range(1, len(arr)):
		for j in range(i - 1, -1, -1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# sort_test(insertion_sort)
sort_test(insertion_sort_2)
