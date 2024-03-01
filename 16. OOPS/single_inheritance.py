class Animal:
    def eat(self):
        print("I can eat")

    def display(self):
        print("I am an animal")


class Dog(Animal):
    def eat(self):
        print("I eat bones")

    def display(self):
        print("I am an dog")


labrador = Dog()
labrador.eat()
labrador.display()
