"""
hdwjakh
dhwajklh dwahkdh awjkd
dhwajkldhwakj
q
"""


def writeIntoFile(filename):
    with open(filename + ".txt", "w") as file:
        while True:
            user_input = input("Enter data = ")
            if user_input.lower() == "q":
                break
            file.write(user_input + "\n")


writeIntoFile("result")
