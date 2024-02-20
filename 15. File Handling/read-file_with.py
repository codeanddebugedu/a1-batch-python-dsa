# file = open("hello.txt", "r")
# data = file.read()
# print(data)
# file.close()

with open("hello.txt") as file:
    data = file.read()
    print(data)

print(file.read())
