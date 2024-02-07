marks = {
    "physics": 43,
    "chemistry": 91,
    "maths": 84,
    "english": 0,
}

# print(marks["physicss"])
# print(marks.get("physicss"))

user_key = input("Enter a key name = ")

result = marks.get(user_key, None)
print(result)

# if result:
#     print(result)
# else:
#     print("Key not found")


# if result != None:
#     print(result)
# else:
#     print("Key not found")

# membership in, not in
# if user_key in marks:
#     print(marks[user_key])
# else:
#     print("Key does not exists")

# if user_key in marks.keys():
#     print(marks[user_key])
# else:
#     print("Key does not exists")
