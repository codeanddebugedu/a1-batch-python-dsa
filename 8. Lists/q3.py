a = [23, 23, 23, 23, 26, 78, 81]  # 7
b = []
# for i in a:
#     if i == 23:
#         a.remove(i)

while a.count(23) > 0:
    a.remove(23)

# for i in range(0, len(a)):
#     if a[i] == 23:
#         a.pop(i)

print(a)
