from book import Book
from library import Library
from member import StudentMember, TeacherMember

library = Library()
members = []

while True:
    print("\n============ LIBRARY MANAGMENT SYSTEM =============")
    print("1. Add book")
    print("2. Display All Books")
    print("3. Search Books")
    print("4. Register Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("\nEnter your choice: ")
    #1 ADD Book
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")

        #check for the duplicate ISBN
        if any(book.isbn for book in library.books):
            print("A book with this ISBN already exists.")
        else:
            book = Book(title, author, isbn)
            library.add(book)

    # 2. Display All Books
    elif choice == "2":
        library.display_books()

    # 3. Search Book
    elif choice == "3":
        title = input("Enter book title to search: ")
        library.search_book(title)

    # Register member 
    elif choice == '4':
        name = input("Enter member name: ")
        member_id = input("enter member id: ")

        #check for dupulicate member id
        if any(member.member_id == member_id for member in members):
            print('a member with htis ID already exists.')
        else: 
            print("\nSelect the member Type: ")
            print("1. Student")
            print("2. Teacher ")

            member_type = input("Enter you choice: ")

            if member_type == "1":
                member = StudentMember(name, member_id)
                members.append(member)
                print(f"Student {name} registered successfully.")

            elif member_type == "2":
                member = TeacherMember(name, member_id)
                members.append(member)
                print(f"Teacher {name} registered successfully.")

            else:
                print("Invalid member type.")

    #5 Borrow Book
    elif choice == '5':
        member_id = input("Enter member ID: ")
        isbn = input("Enter book ISBN: ")

        # Find member
        member = None
        for m in members:
            if m.member_id == member_id:
                member = m
                break

        # Find book
        book = None
        for b in library.books:
            if b.isbn == isbn:
                book = b
                break

        if member is None:
            print("Member not found.")

        elif book is None:
            print("Book not found.")

        else:
            member.borrow_book(book)

    #6. Return book
    elif choice == "6":
        member_id = input("Enter member ID: ")
        isbn = input("Enter book ISBN: ")

        # Find member
        member = None
        for m in members:
            if m.member_id == member_id:
                member = m
                break

        # Find book
        book = None
        for b in library.books:
            if b.isbn == isbn:
                book = b
                break

        if member is None:
            print("Member not found.")

        elif book is None:
            print("Book not found.")

        else:
            member.return_book(book)

     # 7. Exit
    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

