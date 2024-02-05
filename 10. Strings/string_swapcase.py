my_string = "pyTH@#on is GOO!@d"

result = ""

for i in my_string:
    if i.isalpha():
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
    else:
        result += i
print(result)
