# Encapsulation (Public, Private, Protected (access modifiers))
class Person:
    def __init__(self) -> None:
        # Data Members
        self.first_name = input("Enter first name = ")
        self.last_name = input("Enter last name = ")
        self.phone_number = int(input("Enter phone number = "))

    def displayDetails(self):
        print(f"My first name is {self.first_name}")
        print(f"My last name is {self.last_name}")
        print(f"My number is {self.phone_number}")


obj = Person()
print(obj.first_name)
obj.first_name = "xyzxyzxyz"
print(obj.first_name)
