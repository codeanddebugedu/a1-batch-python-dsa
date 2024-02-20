class Student:
    # Constructor
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.phone = int(input("Enter phone = "))

    def update(self):
        phone = int(input("Enter new number = "))
        if len(str(phone)) == 10:
            self.phone = phone
        else:
            print("Invalid Number")

    # Methods
    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")
        print(f"My phone is {self.phone}")


s1 = Student()
s1.display()

s1.update()
s1.display()
