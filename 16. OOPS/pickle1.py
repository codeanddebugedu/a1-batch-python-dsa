import pickle

# a = {"name": "Anirudh", "age": 16}
# a = 55

# with open("result.txt", "wb") as f:
#     pickle.dump(a, f)

with open("result.txt", "rb") as f:
    data = pickle.load(f)
    print(data)
    print(type(data))

# with open("result.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(data[0])
#     print(data[-1])
#     print(type(data))
