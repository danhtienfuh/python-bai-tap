bien_so = int(input())
tong_sum = 0
while(bien_so) :
    chu_so = bien_so % 10
    tong_sum += chu_so
    bien_so //= 10
so_nut = tong_sum % 10
print(so_nut)
if tong_sum == 9 :
    print("may man")
else :
    print("chua may man")