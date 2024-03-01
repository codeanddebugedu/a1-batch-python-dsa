def calculateTotalCost(*args, **kwargs):
    print(kwargs)
    discount = kwargs["discount"]
    if len(args) == 0 or discount > 100 or discount < 0:
        print("Invalid bills or discount")
        return
    totalBill = sum(args)
    discountAmount = (discount / 100) * totalBill

    print(f"Total bill is {totalBill}")
    print(f"Your discount is {discount}%")
    print(f"discount amount is {discountAmount}")
    print(f"final bill is {totalBill-discountAmount}")


calculateTotalCost(100, 200, 300, discount=30)
