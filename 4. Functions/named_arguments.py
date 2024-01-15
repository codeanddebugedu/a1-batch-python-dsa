def marks(physics, chemistry, english, science, hindi):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"Your total marks = {total}")
    print(f"Your percentage scored = {per:.2f}")


# marks(67, 45, 32, 12, 99)
# marks(english=10, hindi=99, physics=67, chemistry=67, science=91)

marks(67, 99, hindi=100, science=11, english=44)
