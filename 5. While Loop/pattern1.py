# 1 11 101 1001 10001 100001 1000001

i = 1
num = 0
while i <= 10:
    print(num + 1, end=" ")
    if num == 0:
        num = 10
    else:
        num = num * 10
    i += 1
