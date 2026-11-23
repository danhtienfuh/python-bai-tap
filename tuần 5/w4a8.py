def reverse_number(x):
    result = 0
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    return result

def is_palindrome(x):
    return x == reverse_number(x)

n = int(input())
steps = 0

while not is_palindrome(n):
    n += reverse_number(n)
    steps += 1

print(steps)
print(n)
