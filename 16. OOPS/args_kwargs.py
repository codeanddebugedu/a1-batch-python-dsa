# Args Kwargs (function/methods)


def add(address, phone, *args, name="", age=0, **kwargs):
    print(f"Args = {args}")
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"Kwargs = {kwargs}")


add("Surat", 97144, 1, 2, 3, name="Akul", x=66, age=44, gender="Male")
