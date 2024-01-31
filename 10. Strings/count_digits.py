a = "my age is 27 and phohdjk463278bvdkl,&*(^&%11)"


count = 0
for ch in a:
    if ord(ch) >= 48 and ord(ch) <= 57:
        count += 1

print(count)
