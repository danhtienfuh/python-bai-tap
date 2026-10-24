a = int(input())
res = 0 
for i in range(1,a+1) :
    if(i % 3 == 0) :
        res += 1
print(res)