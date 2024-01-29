# Deep copy
import copy

my_list = [34, 77, 11, [100, 200, 300], 89, 91, "Anirudh"]
print(my_list)
print(f"{id(my_list) = }")
print(f"{id(my_list[3]) = }")

a = copy.deepcopy(my_list)


a[3][0] = 1
print()
print(my_list)
print(a)
print(id(a))
print(id(a[3]))
