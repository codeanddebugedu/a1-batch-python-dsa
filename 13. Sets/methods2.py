a = {1, 2, 3, 4, 5, "Anirudh", 66.77}
b = {3, 4, 5, 6, 7, 8}

# x = a.union(b)  # All elements from both sets
# print(x)
# x = a.intersection(b)  # Common elements
# print(x)

# x = a.difference(b)
# print(x)
# x = b.difference(a)
# print(x)
print(f"{a = }")
print(f"{b = }")
# a.difference_update(b)
a.intersection_update(b)
print(f"{a = }")
print(f"{b = }")
