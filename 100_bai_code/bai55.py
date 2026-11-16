import sys

a = list(map(int, sys.stdin.read().split()))
values = sorted(set(a), reverse=True)

print(values[1] if len(values) >= 2 else "-")
