from random import randint
from typing import List

"""
Dunder Methods
__<name>__
"""


class Banking:
    """Handles different operations related to banking"""

    def __init__(self, holder_name: str, account_type: str) -> None:
        self.holder_name: str = holder_name.title()
        self.account_type: str = account_type.title()
        self.account_number: int = randint(100000, 999999)
        self.balance: float = 0.0

    def __str__(self) -> str:
        return f"{self.holder_name} (Balance = {self.balance})"

    def __len__(self) -> int:
        return self.account_number

    def __add__(self, other: "Banking") -> float:
        total = self.balance + other.balance
        return total

    def getBalance(self) -> float:
        return self.balance

    def displayDetails(self) -> None:
        """Display all details related to a particular user"""
        print("\n------DETAILS------")
        print(f"Account number = {self.account_number}")
        print(f"Holder name = {self.holder_name}")
        print(f"Account Type name = {self.account_type}")
        print(f"Balance = {self.balance}\n")

    def withdraw(self, amt) -> None:
        if amt > self.balance:
            print("Insufficient balance in your bank")
            return

        self.balance = self.balance - amt
        print(f"Remaining balance = {self.balance}")

    def deposit(self, amt: float) -> None:
        self.balance += amt
        print(f"Remaining balance = {self.balance}")


if __name__ == "__main__":
    obj1 = Banking("Anirudh", "Savings")
    obj2 = Banking("Akul", "Current")
    obj3 = Banking("Vandana", "Saving")
    obj1.balance = 1000
    obj2.balance = 8500
    obj3.balance = 10000
    print(obj1.balance + obj2.balance + obj3.balance)
    print(obj1 + obj2)
