
# Library Management System

## Student Information
- **Full Name:** Mignot Tilahun
- **Assignment Title:** Library Management System – Python OOP Mini Project

## 1. Project Description

The Library Management System is a menu-driven Python application developed to manage books and library members.

The application allows users to add books, display all available books, search for books, register student and teacher members, borrow books, and return borrowed books.

The project is developed using Python Object-Oriented Programming (OOP) principles. It demonstrates how classes and objects can be used to organize code and model a real-world library system.

## 2. OOP Concepts Demonstrated

This project demonstrates the following Object-Oriented Programming concepts:

### 1. Encapsulation
Classes group related data and methods together.

For example:
- The `Book` class manages book information and availability.
- The `Member` class manages member information and borrowed books.
- The `Library` class manages the collection of books.

### 2. Inheritance
The `StudentMember` and `TeacherMember` classes inherit from the `Member` parent class.

This allows both member types to reuse the attributes and methods defined in the parent class.

### 3. Polymorphism
Method overriding is demonstrated through the `borrow_book()` method.

The `StudentMember` and `TeacherMember` classes override the parent class method to implement different borrowing limits.

- Students can borrow up to 5 books.
- Teachers can borrow up to 10 books.

### 4. Abstraction
The application separates responsibilities into different classes and modules, allowing users to interact with library operations without needing to understand their internal implementation.

## 3. Project Structure

```text
LibraryManagement/
│
├── main.py
├── books.py
├── library.py
├── member.py
└── README.md
```

### File Descriptions

- **main.py:** Contains the main program, menu, and user interaction.
- **books.py:** Defines the `Book` class and manages book information and availability.
- **library.py:** Defines the `Library` class and manages adding, removing, displaying, and searching for books.
- **member.py:** Defines the `Member`, `StudentMember`, and `TeacherMember` classes and handles borrowing and returning books.
- **README.md:** Provides project documentation and instructions.

## 4. Features

The application supports the following operations:

1. Add Book
2. Display All Books
3. Search Book
4. Register Member
5. Borrow Book
6. Return Book
7. Exit

### Member Types

| Member Type | Borrowing Limit |
|---|---:|
| Student Member | 5 books |
| Teacher Member | 10 books |

## 5. Requirements

- Python 3.x
- A code editor such as Visual Studio Code
- Terminal or command prompt

No external Python libraries are required.

## 6. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/mignot10/Akiba
```

### Step 2: Navigate to the Project Directory

```bash
cd LibraryManagement
```

### Step 3: Run the Application

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## 7. Mini-Project Explanation

The Library Management System is designed using multiple classes, each responsible for a specific part of the application.

### Book Class
The `Book` class represents individual books and stores their title, author, ISBN, and availability status.

It provides methods to update book availability and display book information.

### Library Class
The `Library` class manages the collection of books.

It provides methods to:
- Add books.
- Remove books.
- Display all books.
- Search for books by title.

### Member Class
The `Member` class represents registered library members.

It stores member information and maintains a collection of borrowed books.

It also provides methods to borrow and return books.

### StudentMember and TeacherMember Classes
These classes inherit from the `Member` class.

They demonstrate inheritance and method overriding by implementing different borrowing limits.

### Main Program
The `main.py` file connects all the classes and provides a menu-driven interface through which users can interact with the system.

## 8. Conclusion

This project demonstrates the practical application of Python Object-Oriented Programming concepts in developing a simple Library Management System.

Through this project, I practiced designing classes, creating objects, implementing inheritance, overriding methods, and organizing a Python application into multiple modules.

