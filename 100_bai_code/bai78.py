s = input().lower()
counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

print(" ".join(f"{ch}:{count}" for ch, count in counts.items()))
