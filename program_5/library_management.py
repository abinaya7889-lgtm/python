class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print(self.title, "was not issued.")


class User:
    def __init__(self, name):
        self.name = name

    def issue(self, book):
        print(self.name, "requested a book.")
        book.issue_book()

    def return_book(self, book):
        print(self.name, "returned a book.")
        book.return_book()


book1 = Book("Python Programming", "John Smith")
user1 = User("Abinaya")

user1.issue(book1)
user1.return_book(book1)