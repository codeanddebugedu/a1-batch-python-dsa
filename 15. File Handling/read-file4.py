f = open("hello.txt", "r")
x = f.read()

count = 0
for ch in x:
    if ch != " " and ch != "\n":
        count += 1

print(count)

f.close()
