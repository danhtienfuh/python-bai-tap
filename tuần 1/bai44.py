matrix = []
n = int(input())
summatrix = 0
matrix = list(map(int, input().split()))
even_sum = 0
for i in range (0,n,2) :
    even_sum += matrix[i]
print(even_sum)