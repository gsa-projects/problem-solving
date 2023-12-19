n = int(input())

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def dfs(num, depth):
    if depth == n:
        print(num)
        return

    for i in range(1, 10):
        new = num + i * 10**depth
        if is_prime(new):
            dfs(new, depth + 1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
