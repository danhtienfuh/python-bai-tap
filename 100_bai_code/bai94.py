from fractions import Fraction

def format_fraction(value):
    numerator = value.numerator
    denominator = value.denominator

    if numerator > denominator:
        whole = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return str(whole)
        return f"{whole},{remainder}/{denominator}"

    return f"{numerator}/{denominator}"

a, b = map(int, input().split())
c, d = map(int, input().split())

f1 = Fraction(a, b)
f2 = Fraction(c, d)

print(format_fraction(f1 + f2))
print(format_fraction(f1 - f2))
print(format_fraction(f1 * f2))
print(format_fraction(f1 / f2))
