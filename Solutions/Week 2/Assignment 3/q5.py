def printPattern(num: int):
    if num > 0:
        start: int = -num
        end: int = num
    else:
        start: int = num
        end: int = -num
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


printPattern(-9)
