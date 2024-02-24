# Ways to sort list of dictionaries by values in Python – Using lambda function.

list_of_dicts = [
    {"name": "Anirudh", "age": 25},
    {"name": "Nihar", "age": 20},
    {"name": "Prem", "age": 30},
]

sorted_list = sorted(list_of_dicts, key=lambda x: x["age"])

print(f"Sorted list of dictionaries by 'age' = {sorted_list}")
