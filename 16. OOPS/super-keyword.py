class Parent:
    def display(self):
        print("I am display method of parent")


class Child(Parent):
    def display(self):
        print("I am display method of child")

    def displayParentInfo(self):
        super().display()


obj = Child()
# obj.display()
obj.displayParentInfo()
