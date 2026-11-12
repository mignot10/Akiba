class Book:
    def __init__(self,title, author, isbn, is_available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def update_available(self):
         self.is_available = not self.is_available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available: {self.is_available}")

