
n,x = map(int,input().split())
matrix = list(map(int,input().split()))
for k in range (0,n) :
    if(matrix[k]==x):
        print("YES")
        print(k)
        break
    else :
        print("NO")
        break 