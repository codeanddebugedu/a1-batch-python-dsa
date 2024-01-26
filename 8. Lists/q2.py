my_list = [54, 32, 92, 92, 45, 46, 22, 22, 54, 54, 11, 10, 92]
my_list2 = []

for i in my_list:
    if i not in my_list2:
        my_list2.append(i)

print(my_list)
print(my_list2)
