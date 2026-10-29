matrix = []
n = int(input())
summatrix = 0
matrix = list(map(int, input().split()))
even = 0
for x in matrix :
    if (not (x % 2)):
        even += 1
print(even)