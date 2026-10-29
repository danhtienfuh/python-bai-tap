nam_nhuan = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nam_khong_nhuan = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
thang , nam = map(int,input().split())
if ( nam % 400 == 0 or nam % 4 == 0 ) and nam % 100 != 0 :
    print(nam_nhuan[thang])
else :
    print(nam_khong_nhuan[thang])
