def min_two(a, b):
    return a if a < b else b

a, b, c = map(int, input().split())

print(min_two(min_two(a, b), c))
