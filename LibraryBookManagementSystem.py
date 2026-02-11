class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("\nYou have successfully borrowed the book.")
        else:
            print("\nSorry, the book is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("\nYou have successfully returned the book.")
        else:
            print("\nThe book is already available in the library.")

    def is_available(self):
        return self.available

    def display_info(self):
        print("\n--- Book Information ---")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.year)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")


# ----- Main Program -----
title = input("Enter book title: ")
author = input("Enter author name: ")
year = input("Enter publication year: ")

book = Book(title, author, year)

while True:
    print("\nChoose an action:")
    print("1 - Borrow Book")
    print("2 - Return Book")
    print("3 - Display Book Information")
    print("4 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.borrow_book()
    elif choice == "2":
        book.return_book()
    elif choice == "3":
        book.display_info()
    elif choice == "4":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
