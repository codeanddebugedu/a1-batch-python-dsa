"""
printNumbers(10,15)
10 11 12 13 14 15

printNumbers(14, 11)
11 12 13 14

printNumbers(7, 4)
4 5 6 7

printNumbers(10,10)
10
"""


# def printNumbers(n1, n2):
#     if n1 < n2:
#         i = n1
#         while i <= n2:
#             print(i, end=" ")
#             i += 1
#         print()
#     elif n2 < n1:
#         i = n2
#         while i <= n1:
#             print(i, end=" ")
#             i += 1
#         print()
#     else:
#         print(n1)


def printNumbers(n1, n2):
    start = n1 if n1 < n2 else n2  # 10
    end = n2 if n1 < n2 else n1  # 10
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printNumbers(10, 10)
# printNumbers(9, 3)
