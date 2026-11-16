k, x = map(int, input().split())
total = 0

for _ in range(k):
    a, n = map(int, input().split())
    total += a * (x ** n)

print(total)
