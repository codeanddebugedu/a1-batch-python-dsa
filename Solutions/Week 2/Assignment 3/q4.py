def calSum(n1: int, n2: int) -> int:
    total: int = 0
    i: int = n1
    while i <= n2:
        if i % 5 == 0:
            total = total + i
        i += 1
    return total


ans = calSum(43, 68)
print(ans)
