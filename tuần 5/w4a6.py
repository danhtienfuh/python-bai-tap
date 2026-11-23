# W4A6 - SumPrimesInRange
# Moi dong input gom hai so a, b; xu ly den het du lieu (EOF).
import sys

def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b = map(int, line.split())
    total = 0
    for x in range(a, b + 1):
        if is_prime(x):
            total += x
    print(total)
