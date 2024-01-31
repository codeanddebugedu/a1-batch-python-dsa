"""
Make two lists of same length and pass it to a function. 
Return a third list where each element is the sum of index. Use List Comprehension
"""
from typing import List


def sumOfList(list1: List[int], list2: List[int]):
    if len(list1) != len(list2):
        print("Lists must have the same length")
        return

    return [list1[i] + list2[i] for i in range(len(list1))]


# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = sumOfList(list1, list2)
print(result)
