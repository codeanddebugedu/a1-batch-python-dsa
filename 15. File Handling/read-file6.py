file = open("hello.txt", "rt")

count = 0
for i in file:
    count += 1

print(count)

file.close()
