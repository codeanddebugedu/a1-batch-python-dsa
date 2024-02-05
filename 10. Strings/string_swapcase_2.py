my_string = "apyTH@#on is GOO!@d"

result = ""


for i in my_string:
    ascii_code = ord(i)
    if ascii_code >= 97 and ascii_code <= 122:
        capital_letter = chr(ascii_code - 32)
        result += capital_letter
    elif ascii_code >= 65 and ascii_code <= 90:
        small_letter = chr(ascii_code + 32)
        result += small_letter
    else:
        result += i

print(result)
