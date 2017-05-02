#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastn = number % 10
elif number < 0 and number % 10 != 0:
    lastn = (10 - (number % 10)) * -1
else:
    lastn = 0
if lastn > 5:
    print('Last digit of', number, 'is', lastn, 'and is greater than 5')
elif lastn == 0:
    print('Last digit of', number, 'is', lastn, 'and is 0')
elif lastn < 6 and lastn != 0:
    print('Last digit of', number, 'is', lastn, 'and is less than 6 and not 0')
