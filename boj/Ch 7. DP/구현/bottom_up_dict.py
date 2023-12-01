import time
from contextlib import contextmanager

@contextmanager
def timing(fmt: str):
    start = time.time()
    yield
    end = time.time()
    print(fmt % (end - start))

n = int(input())
dp = {0: 1, 1: 1}

def fibo(n):
    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

with timing("Runtime: %.3fs"):
    print(fibo(n))
