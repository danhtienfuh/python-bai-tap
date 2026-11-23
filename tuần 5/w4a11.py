# W4A11 - EvenDivisors
n = int(input())
count = 0

for d in range(2, n + 1, 2):
    if n % d == 0:
        count += 1

print(count)
