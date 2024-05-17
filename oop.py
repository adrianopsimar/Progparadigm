class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print(f"No books found with the title '{title}'.")
        else:
            for book in found_books:
                print(book)

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if not found_books:
            print(f"No books found by the author '{author}'.")
        else:
            for book in found_books:
                print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Search for a book by title")
        print("4. Search for a book by author")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            genre = input("Enter the book genre: ").strip()
            new_book = Book(title, author, genre)
            library.add_book(new_book)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            title = input("Enter the book title to search for: ").strip()
            library.search_by_title(title)
        elif choice == '4':
            author = input("Enter the book author to search for: ").strip()
            library.search_by_author(author)
        elif choice == '5':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
