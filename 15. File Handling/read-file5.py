"""
good morning hello
ok bye
done
have a great day


hello morning good
bye ok
done
day great a have

"""

f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    words = line.strip().split()[::-1]
    print(" ".join(i for i in words))


f.close()
