string = "python is a coding language"
x = list(string)
print(x)

x[0] = "Z"
print(x)
print(type(x))

r = "".join(i for i in x[::-1])
# r = "".join(i for i in x)
print(r)
print(type(r))
