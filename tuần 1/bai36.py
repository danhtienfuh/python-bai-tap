a,b = map(int,input().split())

while(b) : 
    r = a % b
    a = b
    b = r

print(a)