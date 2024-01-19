def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 1
        i += 1


pattern(10)
