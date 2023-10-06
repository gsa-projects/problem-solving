from kit import sort_test

def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(n-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print(f'step {i:02d} :', arr)
    
    return arr

sort_test(bubble_sort)
