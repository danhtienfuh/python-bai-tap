def draw_rectangle(d, r):
    if r <= 0 or d <= 0:
        return
    if r == 1:
        print("*" * d)
        return
    print("*" * d)
    for _ in range(r - 2):
        if d == 1:
            print("*")
        else:
            print("*" + " " * (d - 2) + "*")
    print("*" * d)

d, r = map(int, input().split())
draw_rectangle(d, r)
