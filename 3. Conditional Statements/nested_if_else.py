"""
ASk a number from user.

>0 -> POSITIVE
<0 -> NEGATIVE

=0 -> Equal to zero

Nested IF-ELSE
"""
num: int = -55

if num >= 0:
    if num == 0:
        print("Equal to zero")
    else:
        print("Positive")
else:
    print("Negative")
