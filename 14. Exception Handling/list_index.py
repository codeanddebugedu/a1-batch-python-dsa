try:
    my_list = [43, 54, 32, 1, 77]
    index = int(input("Enter index = "))  # 2
    print(my_list[index])
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Some error occurred")
