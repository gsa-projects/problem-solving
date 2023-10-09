from kit import sort_test

def quick_sort2(X):
    if len(X) <= 1:
        return X

    pivot = X[len(X) // 2]
    left = [x for x in X if x < pivot]
    middle = [x for x in X if x == pivot]
    right = [x for x in X if x > pivot]

    return quick_sort2(left) + middle + quick_sort2(right)

sort_test(quick_sort2)
