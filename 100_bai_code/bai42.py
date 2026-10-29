matrix = []
n = int(input())
summatrix = 0
matrix = list(map(int, input().split()))
count = 0
for i in matrix :
    if i > 0 : count += 1
print(count)