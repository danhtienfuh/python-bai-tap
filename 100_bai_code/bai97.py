import sys
import math

a = list(map(int, sys.stdin.read().split()))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

count = sum(1 for x in a if is_prime(x))
print(count if count else "-")
