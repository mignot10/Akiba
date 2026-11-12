class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def remove(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book.title}' has been removed.")
        else:
            print("Book not found in the library.")

    def display_books(self):
        if not self.books:
            print("There is no books in the library.")
            return
        
        for book in self.books:
            book.display_info()
            print('-' * 30)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book found:")
                book.display_info()
                return
        print("Book not found.")