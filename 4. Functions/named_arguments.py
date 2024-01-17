def marks(physics=0, chemistry=0, english=0, science=0, hindi=0):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"Your total marks = {total}")
    print(f"Your percentage scored = {per:.2f}")


# marks(67, 45, 32, 12, 99)
# marks(english=10, hindi=99, physics=67, chemistry=67, science=91)

marks(chemistry=22, physics=67, hindi=100, science=11, english=44)
