# To create list

# a = [i + 5 for i in range(1, 11)]
# a = [f"odd{i}" for i in range(1, 11)]
a = [i % 2 == 0 for i in range(1, 11)]
# for i in range(1, 5000001):
#     a.append(i)


print(a)
