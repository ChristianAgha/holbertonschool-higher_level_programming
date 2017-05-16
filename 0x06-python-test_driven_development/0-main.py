#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(100.3, -2))
print(add_integer(999999999999, 1))
print(add_integer(2 ** 3, 45))
print(add_integer(False, True))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
