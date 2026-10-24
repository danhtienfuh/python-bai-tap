a,b = map(int,input().split())
back_a = a
back_b = b
while (b):
    r = a% b
    a = b
    b = r

ucln = a
back_a //= ucln
back_b //= ucln
print(back_a, end="")
print("/", end="")
print(back_b)