# W4A9 - PerfectSquaresDistinctDigits
n = int(input())
answer = []

x = 0
while x * x <= n:
    square = x * x
    temp = square
    seen = set()
    distinct = True

    if temp == 0:
        seen.add(0)
    while temp > 0:
        digit = temp % 10
        if digit in seen:
            distinct = False
            break
        seen.add(digit)
        temp //= 10

    if distinct:
        answer.append(square)
    x += 1

if answer:
    print(*answer)
else:
    print("(no number)")
