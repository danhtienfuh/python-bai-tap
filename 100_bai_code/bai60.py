import sys
import math

a = list(map(int, sys.stdin.read().split()))
squares = [x for x in a if x >= 0 and math.isqrt(x) ** 2 == x]

if squares:
    print(f"{sum(squares) / len(squares):.1f}")
else:
    print("-")
