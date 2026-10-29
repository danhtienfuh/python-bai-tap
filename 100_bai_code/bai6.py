import math
a,b,c = map(float, input().split())
cv = a + b + c
p = cv / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(round(p,1), round(s,3))


