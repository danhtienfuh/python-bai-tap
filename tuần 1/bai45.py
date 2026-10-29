matrix = []
n = int(input())
summatrix = 0
matrix = list(map(int, input().split()))
even = 0
cur = 0
for x in matrix :
    if (not (x % 2)):
        cur += 1
        even += x
if cur : print(even)
else : print("-")