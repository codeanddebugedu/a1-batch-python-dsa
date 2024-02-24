"""
Python program to find second largest number in a list. 
If 2nd largest element does not exists. Return -1
"""

from typing import List


def findSecondLargest(nums: List[int]) -> int | float:
    if len(nums) < 2:
        return -1

    largest = second_largest = float("-inf")

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        return -1
    else:
        return second_largest


nums = [1, 5, 3, 9, 2, 7]
print(f"Second largest number = {findSecondLargest(nums)}")
