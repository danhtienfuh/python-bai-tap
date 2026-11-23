# W4A12 - Interest
# Lai kep 0.7% moi thang; bo phan le thap phan khi in ket qua.
x, n = map(int, input().split())

for _ in range(n):
    x = int(x * 1.007)

print(x)
