"""
Write a program to find Maximum frequency character in String. 
Return/Print the character which comes the most times in that string.
"""


def maxFrequencyCharacter(string: str) -> str | None:
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    max_freq = 0
    max_freq_char = None
    for char, count in char_count.items():
        if count > max_freq:
            max_freq = count
            max_freq_char = char

    return max_freq_char


s = "hello world"
max_freq_char = maxFrequencyCharacter(s)
if max_freq_char:
    print(f"The character '{max_freq_char}' has maximum frequency in the string.")
else:
    print("There is no character in the string.")
