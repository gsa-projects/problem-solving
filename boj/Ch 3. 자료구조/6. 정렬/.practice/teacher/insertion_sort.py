def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: ', arr)
insertion_sort(arr)
print('정렬 후: ', arr)