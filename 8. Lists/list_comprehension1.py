# Is used to create list
# 1 to 100
def prime(n) -> bool:
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


# my_list = [i for i in range(2, 101) if prime(i) == True]
# print(my_list)

n = 5
my_list = [i * n for i in range(1, 11)]
print(my_list)
