"""
Ask a number from user.

Print YES - if it is divisible by 5 and 6

NO
"""
num: int = int(input("Enter a number = "))

if num % 5 == 0 and num % 6 == 0:
    print("Yes")
else:
    print("No")
