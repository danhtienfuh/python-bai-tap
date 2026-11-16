n = int(input())
a = list(map(int, input().split()))
evens = [x for x in a if x % 2 == 0]

print(f"{sum(evens) / len(evens):.2f}")
