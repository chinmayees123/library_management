# Library Management System

## 1. Project Description
The Library Management System is a simple Python console application used to manage books in a library.
The system allows the user to add books, search for books, issue books, return books, display available books, and save book records.
The project demonstrates Object-Oriented Programming concepts in Python.

## 2. Objectives
The main objectives are:
- To add books to the library.
- To search for books.
- To issue books.
- To return books.
- To display available books.
- To save book records.
- To demonstrate OOP concepts.

## 3. Technologies Used
- Python
- Visual Studio Code
- CSV File Handling
- Object-Oriented Programming

## 4. Main Features
1. Add Book
2. Search Book
3. Issue Book
4. Return Book
5. Display Available Books
6. Save Records
7. Exit

## 5. Classes Used
### Person
`Person` is an abstract base class.
It stores the name of a person and contains the abstract `display()` method.

### Member
`Member` is derived from the `Person` class.
It stores the member ID and name.

### Book
`Book` stores book details such as:
- Book ID
- Title
- Author
- Book status

### FileManager
`FileManager` saves the book records into a CSV file.

## 6. OOP Concepts Used
### Classes and Objects
The project uses classes and objects to represent books and library members.

### Encapsulation
Private attributes are used to store book and member information.
Getter methods are used to access the data.

### Inheritance
The `Member` class inherits from the `Person` class.

### Abstraction
The `Person` class is an abstract class using Python's `abc` module.

### File Handling
Book records are stored in `books.csv`.

### Exception Handling
The program handles invalid inputs and file-related errors.

## 7. How the Project Works
When the program starts, it displays a menu.
The user can select:
- `1` to add a book.
- `2` to search for a book.
- `3` to issue a book.
- `4` to return a book.
- `5` to display available books.
- `6` to save records.
- `7` to exit.

## 8. How to Run
Open the project folder in Visual Studio Code.
Open the terminal and run:
    python library_management.py
The Library Management System menu will appear.
Select an option and follow the instructions.

## 9. Project Files
    Library_Management/
    |
    |-- library_management.py
    |-- books.csv
    |-- README.md
    |
    |-- screenshots/

### library_management.py
Contains the Python source code.

### books.csv
Stores the book records.

### README.md
Contains information about the project.

### screenshots
Contains screenshots of important operations.

## 10. Conclusion
The Library Management System is a simple Python application for managing books.
The project demonstrates classes, objects, encapsulation, inheritance, abstraction, file handling, and exception handling.