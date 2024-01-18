"""
n1 = 30 
n2 = 6


1 to n1 (1 to 30)
Divisible by n2

Calculate total
"""


def calculateFactorsSum(n1, n2):
    i = 1
    total = 0
    while i <= n1:
        if i % n2 == 0:
            total = total + i
        i += 1
    print(total)


calculateFactorsSum(30, 7)
