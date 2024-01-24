"""
Make a function that accepts 2 integer as an argument. (n1,n2)

n1 -> n2
Print prime number

printPrime(2,10)
2 3 5 7

printPrime(50,60)
53 59

Using nested FOR Loop
"""


def printPrime(n1, n2):  # 5 15
    for num in range(n1, n2 + 1):
        factors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factors += 1
        if factors == 2:
            print(num)


printPrime(1, 10)
