class Parent1:
    def func1(self):
        print("I am func1 from parent1")


class Parent2:
    def func1(self):
        print("I am func1 from parent2")


class Child1(Parent1):
    def func4(self):
        print("I am func4 from child1")


class Child2(Child1, Parent2):
    def func(self):
        print("I am func4 from child2")


obj = Child2()
obj.func1()
