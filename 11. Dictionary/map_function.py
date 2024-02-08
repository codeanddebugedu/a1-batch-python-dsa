def convert(n: int):
    if n % 2 == 0:
        return n + 1
    return n - 1


my_list = [34, 54, 17, 65]

x = list(map(convert, my_list))
print(x)
