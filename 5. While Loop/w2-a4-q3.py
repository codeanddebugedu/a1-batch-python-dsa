def pattern(n):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = num * 2
        # num = num + num
        i += 1


pattern(10)
