def prime(n: int) -> bool:
    fact = 0
    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1
    return fact == 2


a = [i for i in range(1, 51) if prime(i)]
print(a)
