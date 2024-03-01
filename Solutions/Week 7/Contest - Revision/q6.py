"""
Write a program for Sum of number digits in List.
"""

from typing import List


def digitSum(num: int) -> int:
    # return sum(int(digit) for digit in str(num))
    total = 0
    n = num
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10
    return total


def sumOfDigitsInList(nums: List[int]) -> List[int]:

    return [digitSum(num) for num in nums]


nums = [12, 66, 3, 20, 21]
print(sumOfDigitsInList(nums))
