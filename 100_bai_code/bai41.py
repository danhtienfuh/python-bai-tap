matrix = []
n = int(input())
summatrix = 0
matrix = list(map(int, input().split()))
for x in matrix:
    summatrix += x

print(summatrix)