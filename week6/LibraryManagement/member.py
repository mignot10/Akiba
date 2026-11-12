class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            print(f"{self.name} has already borrowed {book.title}")
            return

        if not book.is_available:
            print(f"'{book.tile}' is currently unavailable.")
            return
        
        self.borrowed_books.append(book)
        book.update_available()

        print(f"{self.name} borrowed '{book.title}' successfully.")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"{self.name} has not borrowed '{book.title}'.")
            return
        
        self.borrowed_books.remove(book)
        book.update_available()

        print(f"{self.name} returned '{book}'.")

    def display_borrowed_books(self):
        print(f"{self.name} has borrowed the following books:")
        if not self.borrowed_books:
            print("No borrowed books.")
            return
        
        for book in self.borrowed_books:
            print(f"  - {book}")

class StudentMember(Member):
    borrowing_limit = 5

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.borrowing_limit:
           super().borrow_book(book)
        else:
            print(f"{self.name} has reached the borrowing limit({self.borrowing_limit}).")

class TeacherMember(Member):
    borrowing_limit = 10

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.borrowing_limit:
            super().borrow_book(book)
        else: 
            print(f"{self.name} has reached the borrowing limit({self.borrowing_limit}).")