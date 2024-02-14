f = open("hello.txt", "r")
"""# Print how many lines are there
x = f.readlines()
print(len(x))"""

"""
Print how many words are there
"""
lines = f.readlines()
print(lines)
count = 0
for line in lines:
    words = line.strip().split()
    count = count + len(words)
print(count)
f.close()
