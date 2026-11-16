def snt(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

k = int(input())
n = 2

while (k):
    if(snt(n)):
        print(n,end=" ")
        k -=1
    n +=1
   

