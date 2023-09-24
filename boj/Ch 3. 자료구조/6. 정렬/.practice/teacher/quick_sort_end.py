def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = end
    left, right = start, end - 1

    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    arr[left], arr[pivot] = arr[pivot], arr[left]

    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
quick_sort(arr, 0, len(arr) - 1)
print("정렬 후: ", arr)