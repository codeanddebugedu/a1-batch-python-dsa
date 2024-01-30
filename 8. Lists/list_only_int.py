# original_list = [2, 3.75, 0.04, 59.354, 6, 7.7777, 8, 9]
# only_int = [i for i in original_list if type(i) == int]
# only_float = [i for i in original_list if type(i) == float]


# print(only_int)
# print(only_float)


# 1 to 50....2 and 3 divisible
def checkDiv(n: int) -> bool:
    if n % 2 == 0 and n % 3 == 0:
        return True
    else:
        return False


# my_list = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]
my_list = [i for i in range(1, 51) if checkDiv(i) == True]
print(my_list)


# 1 to 50....prime
