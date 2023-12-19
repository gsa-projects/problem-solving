n = int(input())
D = {1: 0}

def f(x: int):
    if x not in D:
        if x % 6 == 0:
            D[x] = min(f(x // 2), f(x // 3)) + 1
        elif x % 3 == 0:
            D[x] = min(f(x // 3), f(x - 1)) + 1
        elif x % 2 == 0:
            D[x] = min(f(x // 2), f(x - 1)) + 1
        else:
            D[x] = f(x - 1) + 1

    return D[x]

print(f(n))
