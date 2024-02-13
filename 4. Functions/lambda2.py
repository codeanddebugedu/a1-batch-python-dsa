# One liner functions


# def addition(n1, n2, n3, n4):
#     return n1 + n2 + n3 + n4


# add1 = lambda n1, n2, n3, n4: n1 + n2 + n3 + n4

# print(add1(10, 20, 30, 40))

# my_list = [
#     {"name": "Anirudh", "age": 67, "marks": [1, 2, 3, 8, 4, 5]},
#     {"name": "dwadwa", "age": 67, "marks": [13, 2, 3, 74, 5]},
#     {"name": "abc", "age": 67, "marks": [14, 2, 35, 94, 5]},
#     {"name": "pqr", "age": 67, "marks": [15, 21, 73, 24, 5]},
#     {"name": "Akul", "age": 67, "marks": [1, 2, 9, 3, 49, 5]},
# ]

# r = list(sorted(my_list, key=lambda x: sum(x["marks"])))
# for details in r:
#     print(details["name"], sum(details["marks"]))


stu_details = {
    "anil": {
        "age": 20,
        "class": "PUC",
        "phone": 8757545,
        "gender": "male",
        "physics": 98,
        "chemistry": 76,
        "maths": 56,
    },
    "sunil": {
        "age": 21,
        "class": "BSC",
        "phone": 9456575,
        "gender": "male",
        "physics": 88,
        "chemistry": 66,
        "maths": 46,
    },
    "amrita": {
        "age": 19,
        "class": "MA",
        "phone": 9856775,
        "gender": "female",
        "physics": 68,
        "chemistry": 56,
        "maths": 36,
    },
    "anand": {
        "age": 22,
        "class": "CS",
        "phone": 93345675,
        "gender": "male",
        "physics": 48,
        "chemistry": 86,
        "maths": 96,
    },
}

x = dict(
    sorted(
        stu_details.items(),
        key=lambda x: x[1]["maths"] + x[1]["chemistry"] + x[1]["physics"],
    )
)
for name, details in x.items():
    total = details["physics"] + details["chemistry"] + details["maths"]
    print(name, total)
