n = int(input())
a = [int(input()) for _ in range(n)]

counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1

best = max(counts, key=counts.get)
print(best, counts[best])
