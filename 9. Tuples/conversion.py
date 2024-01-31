x = (25, 98, 100, 96, 85, 74, "dwadwa")
print(x, id(x))

x = list(x)
x.append(100)
x.append("200")
print(x, id(x))

x = tuple(x)
print(x, id(x))
