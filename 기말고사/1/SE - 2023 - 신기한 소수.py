n = int(input())

# 7331은 신기한 소수다.
# 7 도 소수고
# 73 도 소수고
# 733 도 소수고
# 7331 도 소수기 때문이다.

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

def dfs(num, length):
    if length == n:
        print(num)
        return

    for i in range(1, 10):
        new = num * 10 + i
        if is_prime(new):
            dfs(new, length + 1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
