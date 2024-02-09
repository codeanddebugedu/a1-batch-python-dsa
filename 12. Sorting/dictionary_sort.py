marks = {
    "physics": 43,
    "chemistry": 91,
    "maths": 84,
    "english": 0,
}

print(marks)
sorted_x = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sorted_x)
