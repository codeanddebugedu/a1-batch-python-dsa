class BookStore:
    def __init__(self) -> None:
        self.inventory = {}
        self.sales_data = []

    def displaySalesReport(self):
        totalRevenue = sum([txn["total_price"] for txn in self.sales_data])
        totalBooksSold = sum([txn["quantity"] for txn in self.sales_data])
        print("Revenue Data")
        print(f"Total Revenue: {totalRevenue}")
        print(f"Total Books Sold: {totalBooksSold}")

    def processOrder(self, isbn, customer, quantity):
        if isbn not in self.inventory:
            print("Book not found")
            return
        if quantity > self.inventory[isbn]["quantity"]:
            print("Insufficient quantity available.")
            return
        if quantity <= 0:
            print("Invalid quantity")
            return
        total_price = self.inventory[isbn]["price"] * quantity
        self.inventory[isbn]["quantity"] -= quantity
        data = {
            "isbn": isbn,
            "customer": customer,
            "quantity": quantity,
            "total_price": total_price,
        }
        self.sales_data.append(data)
        print("Order processed successfully.")

    def displayInventory(self):
        if not self.inventory:
            print("No books available in inventory")
            return
        print("Current Inventory:")
        for isbn, details in self.inventory.items():
            print(
                f"ISBN: {isbn}, Name: {details['name']}, Author: {details['author']}, Price: {details['price']}, Quantity: {details['quantity']}"
            )

    def updateQuantity(self, isbn, new_quantity):
        if isbn not in self.inventory:
            print("Book not found")
            return
        if new_quantity < 0:
            print("Invalid quantity")
            return
        self.inventory[isbn]["quantity"] = new_quantity

    def searchBook(self, query):
        foundBooks_ids = []
        for isbn, details in self.inventory.items():
            if query.lower() in [
                str(isbn),
                details["name"].lower(),
                details["author"].lower(),
            ]:
                foundBooks_ids.append(isbn)
        if len(foundBooks_ids) == 0:
            print("No book found with query")
            return

        for ids in foundBooks_ids:
            print(ids, self.inventory[ids])

    def addBook(self, isbn, name, author, price, quantity):
        if isbn in self.inventory:
            print("Book with ISBN already exists")
            return
        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": price,
            "quantity": quantity,
        }


obj = BookStore()

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Generate Sales Report")
    print("6. Display Inventory")
    print("7. Display Sales Data")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        isbn = int(input("Enter ISBN: "))
        name = input("Enter name: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        obj.addBook(isbn, name, author, price, quantity)
        # obj.addBook(quantity=quantity,isbn=isbn)
    elif choice == 2:
        q = input("Search by ISBN/Author/Book name = ")
        obj.searchBook(q)
    elif choice == 3:
        isbn = int(input("Enter ISBN: "))
        quantity = int(input("Enter new quantity: "))
        obj.updateQuantity(isbn, quantity)
    elif choice == 4:
        isbn = int(input("Enter ISBN: "))
        customer = input("Enter customer name = ")
        quantity = int(input("Enter quantity purchased: "))
        obj.processOrder(isbn, customer, quantity)
    elif choice == 6:
        obj.displayInventory()
    elif choice == 5:
        obj.displaySalesReport()
    elif choice == 8:
        break
    else:
        print("Invalid Choice")
