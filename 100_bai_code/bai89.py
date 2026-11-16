def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

m = int(input())
total = 0

for _ in range(m):
    n, k = map(int, input().split())
    total += combination(n, k)

print(total)
