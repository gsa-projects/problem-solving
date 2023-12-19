n = int(input())

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1      # note: i += 1 추가 안해서 무한루프
    return True

def dfs(num, depth):    # note: num 인자의 이름을 n이라고 했어서 깊이 n과 같아져서 탈출 판정이 망함
    if depth == n:
        print(num)
        return

    for i in range(1, 10):
        if is_prime(num * 10 + i):
            dfs(num * 10 + i, depth + 1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
