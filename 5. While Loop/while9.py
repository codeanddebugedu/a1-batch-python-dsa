"""
n1 and n2

Calculate total of all the numbers 
divisible by 3 and 6 between n1 and n2
"""


def calSum(n1: int, n2: int):
    i = n1
    total = 0
    while i <= n2:
        if i % 3 == 0 and i % 6 == 0:
            total = total + i
        i += 1
    return total


x = calSum(1, 20)
print(x)
