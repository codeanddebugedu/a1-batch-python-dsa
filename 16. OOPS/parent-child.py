class Parent:

    def setParentInfo(self):
        self.father_name = input("Enter father_name = ")
        self.mother_name = input("Enter mother_name = ")

    def display(self):
        print(f"My father name is {self.father_name}")
        print(f"My mother name is {self.mother_name}")


class Child(Parent):

    def setChildInfo(self):
        self.setParentInfo()
        self.child_name = input("Enter child_name = ")

    def display(self):
        print(f"My name is {self.child_name}")

    def displayAllDetails2(self):
        print(f"My father name is {self.father_name}")
        print(f"My mother name is {self.mother_name}")
        print(f"My name is {self.child_name}")

    def displayAllDetails(self):
        super().display()
        self.display()


child = Child()
# child.setParentInfo()
child.setChildInfo()
child.displayAllDetails2()
child.displayAllDetails()
