n = int(input())
a = list(map(int, input().split()))

maximum = max(a)
minimum = min(a)

max_positions = [i for i, x in enumerate(a) if x == maximum]
min_positions = [i for i, x in enumerate(a) if x == minimum]

print(maximum, *max_positions)
print(minimum, *min_positions)
