import math

a,b,c = map(int, input().split())
if a + b <= c or a + c <= b or b + c <= a:
    print("Day khong phai la 3 canh cua mot tam giac")
else:
    print("Day la 3 canh cua mot tam giac")
    cv = a + b + c
    p = cv / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"{cv:.2f} {s:.1f}")
