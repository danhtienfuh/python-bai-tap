import sys

a = list(map(int, sys.stdin.read().split()))

print(len(set(a)))
