my_list = [54, 65, 18, 19, 99, 21, 59]

# By Index
# for i in range(0, len(my_list)):
#     print(my_list[i], end=" ")

# By Value
# for i in my_list:
#     print(i, end=" ")

# By Both
for i, j in enumerate(my_list):
    print(f"Index = {i}, value = {j}")
