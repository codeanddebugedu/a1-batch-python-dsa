# Python Program for Find sum of odd factors of a number.
def sumOfOddFactors(n: int) -> int:
    summ = 0
    i = 1
    while i <= n:
        if n % i == 0 and i % 2 != 0:
            summ += i
        i += 1
    return summ


number = int(input("Enter a number: "))
result = sumOfOddFactors(number)
print(result)
