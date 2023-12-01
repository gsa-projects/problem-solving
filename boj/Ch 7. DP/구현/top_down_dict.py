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
    if n not in dp:
        dp[n] = fibo(n - 1) + fibo(n - 2)

    return dp[n]

with timing("Runtime: %.3fs"):
    print(fibo(n))
