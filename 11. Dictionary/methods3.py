marks = {
    "physics": 43,
    "chemistry": 91,
    "maths": 84,
    "english": 0,
    "computer": 44,
}

# x = marks.pop("physicss")
# print(x)
# print(marks)

# To update multiple values
# marks["physics"] = 100
# marks["chemistry"] = 100
# marks["maths"] = 100
marks.update({"physics": 100, "chemistry": 100, "maths": 100, "xyz": 99})
print(marks)
