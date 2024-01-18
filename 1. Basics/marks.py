"""
ASk five marks from user, history /100
Total
Percentage (56.7665434)


Percentage (56.76) (F-STRINGS)
"""
maths = int(input("Enter maths marks = "))
physics = int(input("Enter physics marks = "))
science = int(input("Enter science marks = "))
english = int(input("Enter english marks = "))
hindi = int(input("Enter hindi marks = "))

total = maths + physics + science + english + hindi
print(f"YOur total is = {total}")

percentage = (total / 500) * 100
print(f"Your percentage = {percentage:.4f}")
