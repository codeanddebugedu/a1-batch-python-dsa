"""
Make a function named printMtoN

printMtoN(n1,n2) | n1<n2

printMtoN(1,7)
1 2 3 4 5 6 7


printMtoN(6,13)
6 7 8 9 10 11 12 13
"""


def printMtoN(n1: int, n2: int):
    if n1 > n2:
        print("n1 cannot be greater than n2")
        return
    i = n1
    while i <= n2:
        print(i, end=" ")
        i += 1
    print()


# printMtoN(10, 9)
# printMtoN(3, 7)
printMtoN(7, 3)
# printMtoN(125, 132)
