# Iteration of list
# Iteration by index

# Index = 0 to 9
# How many elements? = 10
lst = [67, 54, 11, 99, 98, 543, 432, "Anirudh", True, 55.556]

# Best
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")

# for i in range(-1, -(len(lst) + 1), -1):
#     print(lst[i], end=" ")


# for i in range(0, len(lst)):
#     print(lst[i], end=" ")

# print()
# for i in range(len(lst)):
#     print(lst[i], end=" ")
