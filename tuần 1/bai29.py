import math
def snt(n):
    if n < 2: 
        return 0
    for i in range (2, int(math.sqrt(n)) + 1) :
        if (n % i == 0):
            return 0
    return 1

n = int(input())
if(snt(n)== 1) : print("YES")
else : print("NO")