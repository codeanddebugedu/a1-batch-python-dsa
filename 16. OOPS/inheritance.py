# class Parent:
#     def display(self):
#         print("I am display of Parent")


# class Child(Parent):
#     def info(self):
#         print("I am info of Child")


# obj = Child()
# obj.info()
# obj.display()


class Animal:
    name = ""

    def eat(self):
        print("I can eat")


class Dog(Animal):

    def bark(self):
        print("I can bark")


class Cat(Animal):

    def meow(self):
        print("I can meow")


labrador = Dog()
labrador.eat()
labrador.bark()
labrador.name = "JJ"
print(labrador.name)

cat = Cat()
cat.eat()
cat.meow()
cat.name = "KK"
print(cat.name)
print(labrador.name)
