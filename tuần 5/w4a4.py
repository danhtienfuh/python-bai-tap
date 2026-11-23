# W4A4 - CountingDigits
# Khong su dung kieu du lieu string.
n = abs(int(input()))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10

print(count)
