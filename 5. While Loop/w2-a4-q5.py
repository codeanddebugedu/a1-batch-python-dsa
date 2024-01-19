count = 0
total = 0
while True:
    num: int = int(input("Enter a Number (enter 0 to finish== )"))
    if num != 0:
        total = total + num
        count = count + 1
    else:
        break
print(total / count)
