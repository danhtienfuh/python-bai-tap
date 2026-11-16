import sys

a = list(map(int, sys.stdin.read().split()))
values = sorted(set(a))

print(values[2] if len(values) >= 3 else "-")
