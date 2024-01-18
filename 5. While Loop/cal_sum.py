"""
Enter a number = 5
Enter a number = -10
Enter a number = 7
Enter a number = 1
Enter a number = 10
Enter a number = 0

Total = 13
"""
total = 0
while 10 > 5:
    num: int = int(input("Enter a number = "))
    total = total + num
    if num == 0:
        break

# print(total)
