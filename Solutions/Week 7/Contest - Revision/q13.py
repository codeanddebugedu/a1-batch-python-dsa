# Write a program to get/print the number of
# characters, words, spaces and lines in a file.


def count(filename: str) -> dict:
    char_count = word_count = space_count = line_count = 0

    with open(filename, "r") as file:
        for line in file:
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())
            space_count += line.count(" ")

    return {
        "characters": char_count,
        "words": word_count,
        "spaces": space_count,
        "lines": line_count,
    }


filename = "hello.txt"
all_count = count(filename)

# Print the results
print(f"Number of characters = {all_count['characters']}")
print(f"Number of words = {all_count['words']}")
print(f"Number of spaces = {all_count['spaces']}")
print(f"Number of lines = {all_count['lines']}")
