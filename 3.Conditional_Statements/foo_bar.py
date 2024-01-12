"""
Ask a number from user.

if num divisible by 3 -> FOO
if num divisible by 5 -> BAR
if num divisible by 3 and 5 -> FOOBAR

FOOFOOBARBAR
"""
num: int = int(input("Enter a number: "))  # 15
if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("FOOFOOBARBAR")
