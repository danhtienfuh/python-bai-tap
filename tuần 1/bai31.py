m,n = map(int,input().split())
pre_3 = 0
for i in range (m ,n + 1) : 
    if (i % 3 == 0) :
        pre_3 += 1
print(pre_3)