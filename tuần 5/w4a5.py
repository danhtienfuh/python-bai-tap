
n = int(input())
found = False

for _ in range(n):
    x = int(input())
    if x == 42:
        found = True

print("I've found the meaning of life!" if found else "It's a joke!")
