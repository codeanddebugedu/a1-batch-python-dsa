my_dict = {"name": "Afsan", "age": 66, "gender": "Male"}

try:
    key_name = input("enter key = ")
    print(my_dict[key_name])
except KeyError:
    print(f"{key_name} is not present in the dictionary")
except:
    print(f"kuch aur error hai")
