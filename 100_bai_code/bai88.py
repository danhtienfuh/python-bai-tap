import math

m, n = map(int, input().split())
g = math.gcd(m, n)

print(f"{m // g}/{n // g}")
