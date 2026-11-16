import math

import math

def input_sides():
    return map(int, input().split())

def perimeter(a, b, c):
    return a + b + c

def area(a, b, c):
    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a, b, c = input_sides()
print(f"{perimeter(a, b, c):.1f} {area(a, b, c):.3f}")
