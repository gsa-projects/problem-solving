n = int(input())
A = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

A.sort()
for m in M:
    flag = False
    i, j = 0, n - 1

    while i <= j:
        mid = (i + j) // 2

        if A[mid] < m:
            i = mid + 1
        elif m < A[mid]:
            j = mid - 1
        else:
            flag = True
            break

    print(int(flag))
