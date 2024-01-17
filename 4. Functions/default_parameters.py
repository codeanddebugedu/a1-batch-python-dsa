# Default Parameters / Required Parameter
def marks(hindi, physics=0, chemistry=0, english=0, science=0):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"Your total marks = {total}")
    print(f"Your percentage scored = {per:.2f}")


# marks(56, 11, 89, 78, 99)
# marks(english=99, hindi=45, chemistry=11, science=34, physics=89)
marks(100)
print()
