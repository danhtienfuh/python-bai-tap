# W4A10 - LongestCollatzUpToN
n = int(input())
best_x = 1
best_length = 1

for start in range(1, n + 1):
    x = start
    length = 1  # Do dai tinh theo so phan tu trong day, ke ca so bat dau va 1.

    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        length += 1

    if length > best_length:
        best_length = length
        best_x = start

print(best_x, best_length)
