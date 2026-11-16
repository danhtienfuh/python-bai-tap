n = int(input())
matrix = list(map(int,input().split()))

for i in matrix :
    if not (i % 5 ) :
        print(i,end=" ")
