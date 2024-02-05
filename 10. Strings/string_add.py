"""
Keep asking characters from user.
Until user tpyes quit

Enter character = a
Enter character = b
Enter character = c
Enter character = d
Enter character = d
Enter character = d
Enter character = e

abcddde
"""

my_string = ""
while True:
    char = input("Enter a char = ")
    if char == "quit":
        break
    my_string += char

print(my_string)
