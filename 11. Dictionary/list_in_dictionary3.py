# anirudh 99
# akul 56
# muskan 98

# With using max(), without using max()

details = {
    "anirudh": [78, 99, 98],
    "akul": [11, 56, 23],
    "muskan": [98, 91, 3],
}


for name, marks in details.items():
    highest_marks = 0
    for i in marks:
        if i > highest_marks:
            highest_marks = i
    print(f"{name} has scored {highest_marks}")

    # print(f"{name} has scored {max(marks)}")
