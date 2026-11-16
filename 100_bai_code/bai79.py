s = input().lower()
counts = {}

for ch in s:
    if ch != " ":
        counts[ch] = counts.get(ch, 0) + 1

best = max(counts, key=counts.get)
print(f"{best}:{counts[best]}")
