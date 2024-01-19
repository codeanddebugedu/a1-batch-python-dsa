def pattern(n):
    num = 1
    i = 1
    while i < n:
        print(num, end=" ")  # 1 3 6 8
        if i % 2 != 0:
            num += 2
        else:
            num += 3
        i += 1


pattern(10)
