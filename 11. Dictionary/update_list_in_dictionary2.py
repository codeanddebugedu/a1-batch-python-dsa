"""
Ask how many students = 2

Enter student name = Anirudh
Enter marks 1 = 56
Enter marks 2 = 13
Enter marks 3 = 98
Enter student name = Akul
Enter marks 1 = 56
Enter marks 2 = 13
Enter marks 3 = 98
"""

dictionary = {}

students_count = int(input("Enter students count = "))
for _ in range(students_count):
    marks = []
    name = input("Enter student name = ")
    subject_count = int(input("Enter subject count = "))
    for i in range(1, subject_count + 1):
        m = int(input(f"Enter marks{i} = "))
        marks.append(m)
    dictionary[name] = marks

print(dictionary)
