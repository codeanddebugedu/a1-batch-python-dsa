"""
Truthy
Falsy 

Values

int -> 5, 6, 999, -15, -85 (truthy)
int -> 0 (falsy)

float -> 56.55, 0.001, -0.00005, -0.00001 (truthy)
float -> 0.0 (falsy)

string -> "anirudh", "x", " " (truthy)
string -> "" (falsy)

boolean -> True (truthy)
boolean -> False (falsy)

"""
# Hello greeting to Anirudh
# No name

name = input("Enter your name = ")
if name:
    print(f"Greeting to {name}")
else:
    print("No name")

# if name != "":
#     print(f"Greeting to {name}")
# else:
#     print("No name")
