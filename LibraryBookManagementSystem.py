class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.year)
        print("Status:", "Available" if self.available else "Borrowed")
        print("------------------------")


# ----- Main Program -----
books = []

while True:
    print("\n===== Library Menu =====")
    print("1 - Add Book")
    print("2 - Borrow Book")
    print("3 - Return Book")
    print("4 - Display All Books")
    print("5 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        
        while True:
            author = input("Enter author name: ")
            if author.replace(" ", "").isalpha():
                break
            else:
                print("Invalid author name. Please use letters only.")

        while True:
            year = input("Enter publication year: ")
            if year.isdigit():
                break
            else:
                print("Invalid year. Please enter numbers only.")

        book = Book(title, author, year)
        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            for i in range(len(books)):
                print(i + 1, "-", books[i].title)

            try:
                num = int(input("Select book number to borrow: ")) - 1
                if 0 <= num < len(books):
                    books[num].borrow_book()
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        if not books:
            print("No books available.")
        else:
            for i in range(len(books)):
                print(i + 1, "-", books[i].title)

            try:
                num = int(input("Select book number to return: ")) - 1
                if 0 <= num < len(books):
                    books[num].return_book()
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not books:
            print("No books added yet.")
        else:
            print("\n--- Library Books ---")
            for book in books:
                book.display_info()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please select from the menu.")
