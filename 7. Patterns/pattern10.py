n = int(input("Enter number of lines = "))  # 13

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
