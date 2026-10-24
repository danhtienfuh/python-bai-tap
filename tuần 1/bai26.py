n = int(input())
sum_3_5 = 0

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0 :
        sum_3_5 += i

print(sum_3_5)