details = {
    "anirudh": [78, 99, 98],
    "akul": [11, 56, 23],
    "muskan": [98, 91, 3],
}

highest_marks = 0
highest_mark_student_name = ""

for k, v in details.items():
    if sum(v) > highest_marks:
        highest_marks = sum(v)
        highest_mark_student_name = k

print(highest_mark_student_name)
print(highest_marks)
