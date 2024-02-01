my_string = input("Enter a string = ")  # ANIrudh

count = 0
for ch in my_string:
    if ch.islower():
        count += 1
    # ascii = ord(ch)
    # if ascii >= 97 and ascii <= 122:
    #     count += 1

print(count)


# if my_string.islower():
#     print("Yes")
# else:
#     print("No")
