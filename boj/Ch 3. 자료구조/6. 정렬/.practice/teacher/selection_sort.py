def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f'step {i+1:02d} :', arr)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print(' 정렬 전 :', arr)
selection_sort(arr)
print(' 정렬 후 :', arr)