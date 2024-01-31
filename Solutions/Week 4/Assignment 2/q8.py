"""
Write a python program which prints all the values whose 
count is greater than 3. 
(Make sure to make a list with at least 15 numbers)

Store them in another list using list comprehension
"""
numbers = [1, 2, 2, 4, 4, 4, 4, 3, 4, 5, 1, 2, 3, 1, 2, 3, 1, 1, 1, 4, 5, 6, 7]

result = []
[result.append(num) for num in numbers if numbers.count(num) > 3 and num not in result]

print(result)
