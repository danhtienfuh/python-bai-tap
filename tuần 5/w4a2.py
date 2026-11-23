# W4A2 - PrimeNumber
# Nhap lai cho den khi nhan duoc mot so nguyen duong.
while True:
    try:
        n = int(input())
        if n > 0:
            break
    except ValueError:
        pass

if n < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not prime")
