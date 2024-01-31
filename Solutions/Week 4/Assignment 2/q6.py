"""
Remove duplicates from the list just by using list comprehension.
"""

"""
Keep in mind, this question is actually not correct
We use list comprehension to create new list and not 
modify the list.

Still you can attempt this question, but there is no proper
solution for this one.
"""

from typing import List


def removeDuplicates(lst: List) -> None:
    result = []
    [result.append(i) for i in lst if i not in result]
    print(result)


my_list = [54, 3, 1, 43, 654, 1, 1, 1, 1, 67, 43, 43, 54, 54]
removeDuplicates(my_list)
