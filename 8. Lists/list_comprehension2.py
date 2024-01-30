# To create new lists
# a = [10, 9,8,7,6...1]

# a = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]


# a = [i for i in range(1, 11) if i % 2 == 0]
# print(a)

# [1,8,9,64....20], odd (square)....even (cube)
a = [i**3 if i % 2 == 0 else i**2 for i in range(1, 21)]
print(a)
