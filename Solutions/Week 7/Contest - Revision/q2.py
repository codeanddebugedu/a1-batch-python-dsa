"""
Write a program to generate a list of even numbers between 1 and 20 
using list comprehension.
"""


def evenNumbers(n1: int, n2: int) -> list[int]:
    return [num for num in range(n1, n2 + 1) if num % 2 == 0]


even_numbers = evenNumbers(1, 21)
print(even_numbers)
