import re

s = input()
print(re.sub(r"(?<=\S) {2,}(?=\S)", " ", s))
