class Student:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.physics = int(input("Enter marks in physics = "))
        self.chemistry = int(input("Enter marks in chemistry = "))
        self.maths = int(input("Enter marks in maths = "))

    def displayName(self) -> None:
        print(f"Name = {self.name}")

    def displayMarks(self) -> None:
        print(f"Physics = {self.physics}")
        print(f"Chemistry = {self.chemistry}")
        print(f"Maths = {self.maths}")

    def updateMarks(self, physics=None, chemistry=None, maths=None):
        if physics:
            self.physics = physics
        if chemistry:
            self.chemistry = chemistry
        if maths:
            self.maths = maths

        # valid_subjects = ["physics", "chemistry", "maths"]
        # user_subject = input("Enter subject name to update = ").lower()

        # if user_subject not in valid_subjects:
        #     print("Invvalid subject")
        #     return

        # new_marks = int(input(f"Enter new {user_subject} marks = "))
        # if user_subject == "physics":
        #     self.physics = new_marks
        # elif user_subject == "chemistry":
        #     self.chemistry = new_marks
        # else:
        #     self.maths = new_marks

    def getTotal(self) -> int:
        return self.physics + self.chemistry + self.maths


s1 = Student()
s1.displayMarks()
print("-----------")
s1.updateMarks(maths=99, chemistry=11)
s1.displayMarks()
