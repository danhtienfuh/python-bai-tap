so_kwh = int(input())
if so_kwh <= 50:
    so_tien = so_kwh * 600
elif so_kwh <= 100:
    so_tien = 50 * 600 + (so_kwh - 50) * 800
elif so_kwh <= 200:
    so_tien = 50 * 600 + 50 * 800 + (so_kwh - 100) * 1100
else:
    so_tien = 50 * 600 + 50 * 800 + 100 * 1100 + (so_kwh - 200) * 1500

print(so_tien)
