# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def show_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 40)


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def show_details(self):
        print(f"Patron ID : {self.patron_id}")
        print(f"Name      : {self.name}")
        if self.borrowed_books:
            print("Borrowed Books :", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books : None")
        print("-" * 40)


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add Book
    def insert_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book.book_id] = book
            print(f"'{book.title}' added successfully.")

    # Register Patron
    def add_patron(self, patron):
        if patron.patron_id in self.patrons:
            print("Patron ID already exists.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"'{patron.name}' registered successfully.")

    # Borrow Book
    def issue_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}' successfully.")

    # Return Book
    def submit_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the patron.")

    # Display Books
    def show_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\n========== Library Books ==========")
        for book in self.books.values():
            book.show_details()

    # Display Patrons
    def show_patrons(self):

        if not self.patrons:
            print("No patrons registered.")
            return

        print("\n========== Registered Patrons ==========")
        for patron in self.patrons.values():
            patron.show_details()


# Main Program
library = Library()

while True:

    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        new_book = Book(book_id, title, author)
        library.insert_book(new_book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        new_patron = Patron(patron_id, name)
        library.add_patron(new_patron)

    elif choice == "3":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.issue_book(patron_id, book_id)

    elif choice == "4":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.submit_book(patron_id, book_id)

    elif choice == "5":
        library.show_books()

    elif choice == "6":
        library.show_patrons()

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
