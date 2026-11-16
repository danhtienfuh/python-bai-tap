def add(a, b):
    return a + b

def divide(a, b):
    return a / b

a, b, c = map(int, input().split())

first = add(add(a, b), c)
second = divide(a, b) + c
third = divide(a, add(b, c))

print(f"{first} {second:.2f} {third:.3f}")
