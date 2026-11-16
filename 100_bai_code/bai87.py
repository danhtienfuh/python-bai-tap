def divisible_by_5(n):
    return n % 5 == 0

n = int(input())

if divisible_by_5(n):
    print("Yes")
else:
    print("No")
