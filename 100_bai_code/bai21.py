km = int(input())
so_tien = 0
if km > 0:
    so_tien = 12000
    km -= 1
    if km <= 29:
        so_tien += km * 10000
    else:
        so_tien += 29 * 10000
        km -= 29
        so_tien += km * 9000

print(so_tien)
