
n = int(input())
largest = 1
p = 2

while p * p <= n:
    while n % p == 0:
        largest = p
        n //= p
    p += 1

if n > 1:
    largest = n  



    
print(largest)
