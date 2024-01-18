def printFactors(num: int):
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print()


def countFactors(num: int):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    print(f"Total factors = {count}")


def checkPrime(num: int):
    i = 1
    factors = 0
    while i <= num:
        if num % i == 0:
            factors = factors + 1
        i += 1
    # ---
    if factors == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")


# countFactors(10)
# countFactors(7)
checkPrime(10)
checkPrime(7)
