"""
Write different ways to remove i'th character from string in Python. Ask 
i from user.
"""


def removeIthCharacter(string: str, i: int) -> None:

    # Method 1: Using slicing
    result_slicing = string[:i] + string[i + 1 :]

    # Method 2: Using string concatenation
    result_concatenation = string[:i] + string[i + 1 :]

    # Method 3: Using string replace() method
    result_replace = string.replace(string[i], "", 1)

    print(result_slicing, result_concatenation, result_replace)


input_string = input("Enter the string: ")
i = int(input("Enter the index of the character to remove: "))

removeIthCharacter(input_string, i)
