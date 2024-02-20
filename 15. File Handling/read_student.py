with open("student.txt") as file:
    # data = file.readlines()
    # print(data)
    roll_no = file.read().split()


with open("student_data.txt") as file:
    student_data = file.readlines()
    for student_roll_no in roll_no:
        for student in student_data:
            detail = student.strip()
            roll, detail = detail.split("-")
            if roll == student_roll_no:
                print(f"{roll} - {detail}")
