from functools import lru_cache
@lru_cache(maxsize = 32)
def fib(n):
    if n > 1:
        n = fib(n-1) + fib(n-2)
    return n
