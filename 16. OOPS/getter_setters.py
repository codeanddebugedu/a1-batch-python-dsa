class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, new_age):
        self.__age = new_age


s1 = Student("Anirudh", 88)
print(s1.get_age())
s1.set_age(100)
# s1._Student__age = 1000  # Name mangling
print(s1.get_age())
