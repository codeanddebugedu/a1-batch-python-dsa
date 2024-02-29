"""Library Management System"""

from random import randint
from typing import List


class Book:
    def __init__(self) -> None:
        self.isbn: int = int(input("Enter ISBN = "))
        self.name: str = input("Enter Name of Book= ")
        self.price: float = float(input("Enter Price of Book= "))
        self.quantity: int = int(input("Enter Quantity of Books= "))
        self.rented: bool = False

    def displayBookInfo(self) -> None:
        print("\n---------Book Details---------")
        print(f"ISBN Number of the Book -> {self.isbn}")
        print(f"Name of the Book-> {self.name}")
        print(f"Price of the Book > {self.price}")
        print(f"Total quantity of The Book {self.quantity}")
        print(f"If any Book is Rented?-> {self.rented}\n")

    def checkQuantityOfBook(self) -> int:

        return self.quantity

    def rentBook(self, rent_quant) -> None:

        if rent_quant > self.quantity:
            print(f"insufficient Stock of {self.isbn}")
            return
        self.rented == True
        self.quantity -= rent_quant
        print(f"Book rent for {rent_quant} successfull")
        print(f"{self.quantity} No of Books Left for {self.isbn}")

    def returningRentedBooks(self, return_quant):
        if self.rented == False:
            print(f"Books are not Rented for {self.isbn}")
            return
        self.quantity += return_quant
        self.rented = True
        print(f"Rented book for {self.isbn} returned")


library: List[Book] = []
while True:
    print(
        """\nPlease Choose a Number from Below options
1.add_Book
2.search_book
3.rent_book
4.display_books
5.return_book
6.check_quantity
7.exit_program\n"""
    )
    choice: int = int(input("Enter Choice = "))
    if choice == 1:
        obj = Book()
        library.append(obj)
        print("\nBook Added to Library")
    elif choice == 2:
        user_isbn = int(input("Enter the ISBN of book to search= "))
        for book in library:
            if book.isbn == user_isbn:
                book.displayBookInfo()
                break
        else:
            print("Book Not found")
    elif choice == 3:
        if len(library) == 0:
            print("No Books Available for Rent")
        else:
            user_isbn = int(input("Enter the ISBN of book to search= "))
            quntity = int(input("Enter No of Books to rent"))
            for book in library:
                if book.isbn == user_isbn:
                    book.rentBook(quntity)
                    break
            else:
                print("Book Not Available for Rent")

    elif choice == 4:
        if len(library) == 0:
            print("No Books to display")

        for book in library:
            book.displayBookInfo()
    elif choice == 5:
        user_isbn = int(input("Enter the ISBN of book to search= "))
        quantity = int(input("Enter No of Books tom return= "))
        for book in library:
            if book.isbn == user_isbn:
                book.returningRentedBooks(quantity)
                break
        else:
            print(f"Book Not availablefor return with {user_isbn} ")
    elif choice == 6:
        user_isbn = int(input("Enter the ISBN of book to search= "))
        for book in library:
            if book.isbn == user_isbn:
                print(book.checkQuantityOfBook())
                break
        else:
            print(f"Book Not availablefor return with {user_isbn} ")
    elif choice == 7:
        print("Tata Bye")
        break
    else:
        print("Invalid Entry")
