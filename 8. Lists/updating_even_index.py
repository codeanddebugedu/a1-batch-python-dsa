# Using function
from typing import List


def evenIndexUpdate(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if i % 2 == 0:
            lst[i] = 0


def evenValueUpdate(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0


my_list = [54, 43, 19, 85, 11, 94, 32, "Anirudh"]
evenIndexUpdate(my_list)
print(my_list)
# Output = [0, 43, 0, 85, 0, 94, 0]
