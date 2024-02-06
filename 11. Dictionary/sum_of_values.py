marks = {
    "physics": 67,
    "comp": 10,
    "science": 99,
    "english": 82,
    "hindi": 17,
}

# print(sum(marks.values()))
total = 0
for mark in marks.values():
    total = total + mark

print(total)
