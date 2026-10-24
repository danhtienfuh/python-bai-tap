m,n = map(int,input().split())
sum_even = 0
cur_35 = 0

for i in range(m,n + 1):
    if i % 3 == 0 or i % 5 == 0 :
        cur_35 += 1
    if i % 2 == 0 :
        sum_even += i
print(cur_35, sum_even)