class Employee:
    def __init__(self) -> None:
        self.name = input("Enter the  name ")
        self.age = input("Enter the age ")
        self.gender = input("Enter the gender ")
        self.phone_number = input("Enter the phone_number ")

    def display(self):
        pass

    def calculate(self):
        hourlyrate = int(input("Enter you hourly rate "))
        hoursworked = int(input("Enter you hours worked "))
        monthly = hourlyrate * hoursworked * 4
        print(f"monthly salary is {monthly}")
        yearly = hourlyrate * hoursworked * 52
        print(f"yearly salary is {yearly}")


e1 = Employee()
e1.calculate()
