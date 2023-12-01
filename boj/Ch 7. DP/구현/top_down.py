import time
from contextlib import contextmanager

@contextmanager
def timing(fmt: str):
    start = time.time()
    yield
    end = time.time()
    print(fmt % (end - start))

n = int(input())
dp = [-1] * (n+1)
dp[0], dp[1] = 0, 1

def fibo(n):
    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

with timing("Runtime: %.3fs"):
    print(fibo(n))
