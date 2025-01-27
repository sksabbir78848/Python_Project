class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Issued: {'Yes' if self.is_issued else 'No'}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.book_id in self.books:
            print(f"Book with ID {book.book_id} already exists.")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added successfully.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book with ID {book_id} has been deleted.")
        else:
            print("Book not found!")

    def issue_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_issued:
                print(f"Book '{book.title}' is already issued.")
            else:
                book.is_issued = True
                print(f"Book '{book.title}' has been issued.")
        else:
            print("Book not found!")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_issued:
                book.is_issued = False
                print(f"Book '{book.title}' has been returned.")
            else:
                print(f"Book '{book.title}' wasn't issued.")
        else:
            print("Book not found!")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nBooks in Library:")
            for book in self.books.values():
                print(book)


def menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. Exit")

def main():
    library = Library()

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == 2:
            book_id = input("Enter Book ID to delete: ")
            library.delete_book(book_id)

        elif choice == 3:
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == 4:
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == 5:
            library.view_books()

        elif choice == 6:
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
