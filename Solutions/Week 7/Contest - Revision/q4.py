"""
Write a function to find the contiguous subarray with the largest 
sum in a given list of integers.
"""


def largestSum(mylist: list[list[int]]):
    largest = float("-inf")
    for lst in mylist:
        if sum(lst) > largest:
            largest = sum(lst)
    return largest


my_list = [[1, 1, 1], [5, 5, 5, 5, 5], [4, 1, 9, 8]]
print(largestSum(my_list))
