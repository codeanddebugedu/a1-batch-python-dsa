a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {4, 5, 6, 7, 8}
d = {4, 5, 6, 7, 8, 100, 200}
x = a | b | c | d
print(x)


x = a.copy()

x.remove(5)
print(x)
print(a)


print(id(a))
print(id(x))
