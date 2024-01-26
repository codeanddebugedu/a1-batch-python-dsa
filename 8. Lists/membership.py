# Membership Operator (IN / NOT IN)

my_list: list[int] = [54, 99, 18, 19, 99, 21, 59, True]

search_number = 99

if search_number in my_list:
    print("Yes")
else:
    print("No")


# if my_list.count(search_number) > 0:
#     print("Yes")
# else:
#     print("No")
