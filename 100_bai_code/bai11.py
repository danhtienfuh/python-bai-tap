a = int(input())
gio = (a // 60) // 60
phut = (a - (gio * 60 *60) )// 60
giay = (a -(gio * 60 * 60)-(phut * 60))
print(gio,":",phut,":",giay)