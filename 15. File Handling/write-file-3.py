"""
hdwjakh
dhwajklh dwahkdh awjkd
dhwajkldhwakj
q
"""


def writeIntoFile(user_input, filename):
    with open(filename + ".txt", "w") as file:
        file.write(user_input)


filename = input("Enter filename without extension = ")
user_in = ""
while True:
    u_inp = input("Enter dataa = ")
    if u_inp.lower() == "q":
        break
    user_in = user_in + u_inp
    user_in = user_in + "\n"

writeIntoFile(user_in[:-1], filename)
