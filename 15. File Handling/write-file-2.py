def writeIntoFile(user_input, filename):
    with open(filename + ".txt", "w") as file:
        file.write(user_input)


user_in = input("Enter input = ")
filename = input("Enter filename without extension = ")

writeIntoFile(user_in, filename)
