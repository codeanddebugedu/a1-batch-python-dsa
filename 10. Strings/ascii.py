a = "python is Ooa cool coding language"

count = 0
for ch in a:
    if ord(ch) == 111 or ord(ch) == 79:
        count += 1

print(count)
