x = input("Enter a number = ")  # one

# If digit, then convert to int, else print INVALID
if x.isdigit():
    x = int(x)
    print(x, type(x))
else:
    print("INVALID")
