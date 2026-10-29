n = int(input())
cur1 = 0
cur2 = 0
matrix = list(map(int,input().split()))
matrix_duong = []
matrix_am = []

for x in matrix :
    if x >0 :
        cur1 += 1
        matrix_duong.append(x)
    else :
        cur2 += 1
        matrix_am.append(x)
print(cur1," ",cur2)
if  not cur1 :
    print("-")
else :
    for x in matrix_duong:
        print(x, end=" ")
print()
if not cur2 :
    print("-")
else :
    for x in matrix_am:
        print(x, end=" ")
