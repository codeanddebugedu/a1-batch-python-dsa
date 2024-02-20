class Product:
    def __init__(self) -> None:
        self.name = input("Enter the  name ")
        self.price = int(input("Enter the price "))
        self.category = input("Enter the category ")
        self.quantity = int(input("Enter the quantity "))

    def calculate(self):
        discountamount = int(input("Enter the discount amount "))
        toatlprice = (self.price - discountamount) * self.quantity
        print(f"total price is {toatlprice}")


p1 = Product()
p1.calculate()
