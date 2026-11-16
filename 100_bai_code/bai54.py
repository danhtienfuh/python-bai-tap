import sys

a = list(map(int, sys.stdin.read().split()))
negatives = [x for x in a if x < 0]

print(max(negatives) if negatives else "-")
