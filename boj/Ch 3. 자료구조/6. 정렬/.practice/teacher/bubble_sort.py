def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(n-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'step {i:02d} :', arr)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = [i for i in range(9, 0, -1)]
print(' 정렬 전 :', arr)
bubble_sort(arr)
print(' 정렬 후 :', arr)