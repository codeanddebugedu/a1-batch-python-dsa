"""
Ask a number from user
Check if number is ODD or EVEN

Ternary Operators
"""


def check(num: int) -> str:
    # print("EVEN") if num % 2 == 0 else print("ODD")
    # if num % 2 == 0:
    #     print("dwadwa")
    #     print("hdkjwahdka")
    #     return "EVEN"
    # else:
    #     return "ODD"
    return "EVEN" if num % 2 == 0 else "ODD"


print(check(10))
print(check(21))
