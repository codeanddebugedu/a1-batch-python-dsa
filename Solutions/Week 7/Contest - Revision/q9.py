"""
Given a string of size n, write functions to perform following operations on string
1. Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
2. Right (Or clockwise) rotate the given string by d elements (where d <= n)
"""


def leftRotate(string: str, d: int) -> str:
    n = len(string)
    d = d % n
    return string[d:] + string[:d]


def rightRotate(string: str, d: int) -> str:
    n = len(input_string)
    d = d % n
    return string[n - d :] + string[: n - d]


input_string = "pythonprogramming"
d = 4
print(f"Left rotated string = {leftRotate(input_string, d)}")
print(f"RIght rotated string = {rightRotate(input_string, d)}")
