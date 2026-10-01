class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued successfully.")
        else:
            print("Book already issued.")

    def return_book(self):
        self.available = True
        print("Book returned successfully.")

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", status)


book = Book("Python Programming")

while True:
    print("\n1. Display Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book.display()

    elif choice == 2:
        book.issue()

    elif choice == 3:
        book.return_book()

    elif choice == 4:
        print("Exiting library...")
        break

    else:
        print("Invalid choice.")