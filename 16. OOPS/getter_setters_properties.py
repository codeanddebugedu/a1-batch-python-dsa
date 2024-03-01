class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    @property
    def age(self):
        print("GETTER METHOD CALLED")
        return self.__age

    @age.setter
    def age(self, new_age, abc):
        print(abc)
        print("SETTER METHOD CALLED")
        if new_age < 18:
            raise ValueError("Less age")
        self.__age = new_age


obj = Student("Anirudh", 100)
print(obj.age)
obj.age = 7, 9
print(obj.age)
