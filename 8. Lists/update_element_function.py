from typing import List

# Pass by value


# Pass by reference
def xyz(gggggg: List) -> None:
    print(id(gggggg))
    gggggg[0] = 100


a: List = [43, 54, 65, 32, 111]
print(id(a))


xyz(a)
print(a)
