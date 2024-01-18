def calSum(n1: int, n2: int):
    if n1 > n2:
        return "n1 should be smaller"
    total: int = 0
    i: int = n1
    while i <= n2:
        total = total + i
        i += 1
    return total


x = calSum(1, 10)
print(x)

x = calSum(7, 3)
print(x)
