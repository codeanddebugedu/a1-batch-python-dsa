"""
Ask 2 numbers from user.

Calculate total

Check if that total is odd/even

total(n1,n2) -> int

check(n1) -> None

"""


def total(num1: int, num2: int) -> int:
    return num1 + num2


def checkEvenOdd(num: int) -> None:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


num1: int = int(input("Enter a number "))
num2: int = int(input("Enter a number "))
checkEvenOdd(total(num1, num2))
