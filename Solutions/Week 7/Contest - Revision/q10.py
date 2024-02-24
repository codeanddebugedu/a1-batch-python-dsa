# Python program to find the sum of all items in a dictionary.


def sum(dictionary: dict) -> int:
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum


my_dictionary = {"a": 10, "b": 20, "c": 30}
sum_of_values = sum(my_dictionary)
print(f"Sum of all items in the dictionary = {sum_of_values}")
