def power(base: int | None = 1, exponent: int | None = None) -> int:
    if base != None and exponent != None:
        return base**exponent
    else:
        return -1


# power(5,3) -> 125
# power(5,None) -> -1
# power(None,None) -> -1
print(power())
