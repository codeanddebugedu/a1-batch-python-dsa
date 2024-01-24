"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

# for j in range(n,i-1,-1) samaj nhi aya,plz batado..confuse hogatya


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


pattern(7)
