# Protected (_), Private (__)


class Company:
    def __init__(self) -> None:
        self._project = "Video Calling App"
        print("I am constructor of Company")


class Employee(Company):
    def __init__(self, name) -> None:
        self.name = name
        print("I am constructor of Employee")
        super().__init__()

    def show(self):
        print(f"Name = {self.name}")
        print(f"I am working on a project named {self._project}")


obj = Employee("Anirudh")
obj.show()
print(obj._project)
obj._project = "XYZ"
print(obj._project)
obj.show()
