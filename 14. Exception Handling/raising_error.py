# Age age from user. Less than 18, Cannot vote
try:
    age = int(input("Enter age = "))
    if age < 18:
        raise ZeroDivisionError
    print("You can vote")
except ZeroDivisionError:
    print("You cannot vote")
except ValueError:
    print("Enter proper age")
except:
    print("Some error")
