# class ABC:
#     def func1(self):
#         print("I am func1 of ABC")


# class PQR:
#     def func2(self):
#         print("I am func2 of PQR")


# class XYZ(ABC, PQR):
#     def func3(self):
#         print("I am func3 of XYZ")


# obj = XYZ()
# obj.func3()
# obj.func1()
# obj.func2()
class ABC:
    def func1(self):
        print("I am func1 of ABC")


class PQR:
    def func1(self):
        print("I am func2 of PQR")


class MNQ:
    def func1(self):
        print("I am func2 of PQR")


class XYZ(PQR, ABC, MNQ):
    def func(self):
        print("I am func3 of XYZ")


obj = XYZ()
obj.func1()
