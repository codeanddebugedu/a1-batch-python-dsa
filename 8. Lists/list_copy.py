my_list = [45, 17, 89, 94, "Anirudh", 55.687, 12.225]
print(my_list)
print(id(my_list))


a = my_list.copy()  # Shallow Copy
# Values copy nahi ki
# Memory/Address copy


print(a)
print(id(a))

a[0] = 1000
my_list[-1] = 1000
print("After changing")
print("my_list =", my_list)
print("a =", a)
