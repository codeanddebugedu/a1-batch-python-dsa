import pickle


class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")


# obj = Student("Anirudh", 99)
# with open("result.txt", "wb") as f:
#     pickle.dump(obj, f)
with open("result.txt", "rb") as f:
    data = pickle.load(f)
    print(data)
    print(data.name)
    print(data.age)
    data.display()
