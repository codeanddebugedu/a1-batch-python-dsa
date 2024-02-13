try:
    a = int(input("Enter number 1 = "))
    b = int(input("Enter number 2 = "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot by zero")
except:
    print("Some error occurred")
else:
    print("Everything works fine")
finally:
    print("This is finally")
