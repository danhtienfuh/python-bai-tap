# W4A13 - ClosePairNumber
def sum_proper_divisors(n):
    if n <= 1:
        return 0

    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            other = n // d
            if other != d:
                total += other
        d += 1
    return total

a, b = map(int, input().split())
print("true" if a != b and sum_proper_divisors(a) == b
      and sum_proper_divisors(b) == a else "false")
