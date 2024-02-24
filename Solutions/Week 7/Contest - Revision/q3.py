"""
Write a function that takes a string as input and returns only vowels in that string
"""


def extractVowels(string: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join([char for char in string if char in vowels])


string = "aeroplaneaaei"
print(extractVowels(string))
