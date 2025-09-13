class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.__copies = copies

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        if value < 0:
            print("❌ Number of copies cannot be negative!")
        else:
            self.__copies = value

    def borrow_book(self, borrowed_copies):
        if borrowed_copies <= self.copies:
            self.copies -= borrowed_copies
            print(f"{borrowed_copies} copies borrowed successfully.")
        else:
            print("❌ Not enough copies available to borrow!")

    def return_book(self, returned_copies):
        self.copies += returned_copies
        print(f"{returned_copies} copies returned successfully.")

    def display_record(self):
        print(f"Book: {self.title} | Author: {self.author} | Copies Available: {self.copies}")

book1 = Book("Clean Code", "Robert C. Martin", 1000)
book2 = Book("Introduction to Algorithms", "Thomas H. Cormen", 500)

book1.borrow_book(100)
book1.display_record()
book1.return_book(50)
book1.display_record()

book2.borrow_book(499)
book2.display_record()
book2.return_book(234)
book2.display_record()