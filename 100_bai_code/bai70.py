s = input()
result = []
capitalize_next = True

for ch in s:
    if ch.isspace():
        result.append(ch)
        capitalize_next = True
    elif capitalize_next:
        result.append(ch.upper())
        capitalize_next = False
    else:
        result.append(ch)

print("".join(result))
