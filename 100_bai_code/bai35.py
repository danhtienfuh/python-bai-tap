import math

def snt(n):
    if n < 2: 
        return 0
    for i in range (2, int(math.sqrt(n)) + 1) :
        if (n % i == 0):
            return 0
    return 1

m,n = map(int,input().split())
tong = 0
cur = 0
for i in range(m,n+1) :
    if(snt(i)) : 
        tong += i
        cur += 1
tbc = tong / cur

print(f"{tbc:.2f}")