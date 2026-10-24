import math

def snt(n):
    if n < 2: 
        return 0
    for i in range (2, int(math.sqrt(n)) + 1) :
        if (n % i == 0):
            return 0
    return 1

m,n = map(int,input().split())
cur_prerix = 0
for i in range (m, n + 1):
    if (snt(i)) : cur_prerix += 1
print(cur_prerix)