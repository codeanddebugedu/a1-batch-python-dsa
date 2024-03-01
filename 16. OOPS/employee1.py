class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name = {self.name} and salary = {self.__salary}")

    def __showSalary(self):
        return self.__salary

    def updateSalary(self, new_salary):
        self.__salary = new_salary


emp = Employee("Anirudh", 1000)
emp.show()
# print(emp.__showSalary())
emp.__salary = 654465465
print(emp.__salary)
# print(emp._Employee__salary)
# print(emp.showSalary())
print("------")
emp.name = "xyzxzy"
emp.show()
emp.updateSalary(10000)
emp.show()
