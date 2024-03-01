class GrandParent:
    def func1(self):
        print("I am func1 of GrandParent")


class Parent(GrandParent):
    def func2(self):
        print("I am func2 of Parent")


class Child(Parent):
    def func3(self):
        print("I am func3 of Child")


obj = Child()
obj.func3()
obj.func2()
obj.func1()
