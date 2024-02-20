class Student:
    def __init__(self) -> None:
        self.name: str = input("Enter name = ")
        self.marks: dict = {"physics": 0, "chemistry": 0, "maths": 0}

    def addSubjectNameWithParam(self, new_sub: str, new_mark: int) -> None:
        if new_sub in self.marks:
            print("Subject already exists")
            return

        self.marks[new_sub] = new_mark

        # if new_sub not in self.marks:
        #     self.marks[new_sub] = new_mark
        # else:
        #     print("Subject already exists")

    def addSubjectWithoutParam(self):
        new_subject_name = input("Enter new subject name = ")
        new_subject_marks = int(input(f"Enter marks of {new_subject_name} = "))
        # self.marks[new_subject_name] = new_subject_marks
        self.marks.update({new_subject_name: new_subject_marks})

    def displayMarks(self):
        for subject_name, marks in self.marks.items():
            print(f"{subject_name} = {marks}")

    def updateMarks(self, subject_name: str):
        if subject_name not in self.marks:
            print("Invalid subject")
            return

        new_marks = int(input(f"Enter new marks of {subject_name}"))
        self.marks[subject_name] = new_marks
        print("Marks updated\n")


s1 = Student()
s1.displayMarks()
print("-----")
s1.addSubjectNameWithParam("history", 88)
s1.displayMarks()
