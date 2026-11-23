# W4A15 - ChickenAndDog
# Input: tong so con va tong so chan.
animals, legs = map(int, input().split())

# Ga co 2 chan, cho co 4 chan.
dogs = (legs - 2 * animals) // 2

if legs % 2 == 0 and 0 <= dogs <= animals:
    chickens = animals - dogs
    if 2 * chickens + 4 * dogs == legs:
        print(chickens, dogs)
    else:
        print("invalid")
else:
    print("invalid")
