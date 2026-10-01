class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book:", self.title)


class PrintedBook(Book):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages

    def display(self):
        print("Printed Book:", self.title)
        print("Pages:", self.pages)


class EBook(Book):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    def display(self):
        print("E-Book:", self.title)
        print("File Size:", self.size, "MB")


book1 = PrintedBook("Data Structures", 450)
book2 = EBook("Python Basics", 5)

book1.display()
book2.display()