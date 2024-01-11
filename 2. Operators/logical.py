"""
AND, OR, NOT (To compare, 2 or more conditions) (answer is always in BOOL)

AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (Ulta kar deta hai)
"""
physics = 17
chemistry = 85

# print(physics >= 33 or chemistry >= 33)  # F or T = T
# print(not physics >= 33)
# print(not (physics >= 33 or chemistry >= 33))  # not T
print(not physics >= 33 or not chemistry >= 33)
# not F or not T
# T or F
# T
