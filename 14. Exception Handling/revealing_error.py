try:
    a = int(input("Enter number 1 = "))
    b = int(input("Enter number 2 = "))
    print(a / b)
except Exception as e:
    print("Some error occurred")
    print(f"Error = {type(e).__name__} and message = {e}")
