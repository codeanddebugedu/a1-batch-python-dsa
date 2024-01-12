"""
Ask a single mark from user
91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
0 - 70 -> FAIL
"""
mark: int = int(input("Enter marks = "))  # 95

if mark >= 91 and mark <= 100:
    print("A")
if mark >= 81 and mark <= 90:
    print("B")

if mark >= 71 and mark <= 80:
    print("C")

if mark >= 0 and mark <= 70:
    print("FAIL")
else:
    print("Invalid marks")

# .........
