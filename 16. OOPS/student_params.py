class Student:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.phone = int(input("Enter phone = "))

    def updateAge(self, new_age: int) -> None:
        self.age = new_age

    def update(self, new_phone):
        if len(str(new_phone)) == 10:
            self.phone = new_phone
        else:
            print("Invalid Number")

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")
        print(f"My phone is {self.phone}")


s1 = Student()
s1.display()
a = int(input("Enter new age = "))
s1.updateAge(a)
s1.display()
