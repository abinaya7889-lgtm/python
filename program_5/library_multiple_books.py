class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "|", self.author, "|", status)

    def issue(self):
        if self.available:
            self.available = False
            print("Issued:", self.title)
        else:
            print("Book unavailable.")


books = [
    Book("Python", "Guido"),
    Book("Java", "James Gosling"),
    Book("C++", "Bjarne Stroustrup")
]

print("Library Books:")

for book in books:
    book.display()

print("\nIssuing Python book:")
books[0].issue()

print("\nUpdated List:")

for book in books:
    book.display()