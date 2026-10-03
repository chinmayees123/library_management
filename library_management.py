import csv
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def display(self):
        pass
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(name)
        self.__member_id = member_id
    def display(self):
        print("Member ID:", self.__member_id)
        print("Name:", self.get_name())
class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__issued = False
    def get_book_id(self):
        return self.__book_id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author
    def issue(self):
        self.__issued = True
    def return_book(self):
        self.__issued = False
    def is_issued(self):
        return self.__issued
    def display(self):
        status = "Issued" if self.__issued else "Available"
        print("Book ID:", self.__book_id)
        print("Title:", self.__title)
        print("Author:", self.__author)
        print("Status:", status)
class FileManager:
    def save(self, books):
        try:
            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Book ID", "Title", "Author", "Status"])
                for book in books:
                    status = "Issued" if book.is_issued() else "Available"
                    writer.writerow([
                        book.get_book_id(),
                        book.get_title(),
                        book.get_author(),
                        status
                    ])
            print("Records saved successfully.")
        except Exception:
            print("Error while saving file.")
books = []
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Save Records")
    print("7. Exit")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book = Book(book_id, title, author)
            books.append(book)
            print("Book added successfully.")
        case "2":
            book_id = input("Enter Book ID: ")
            for book in books:
                if book.get_book_id() == book_id:
                    book.display()
                    break
            else:
                print("Book not found.")
        case "3":
            book_id = input("Enter Book ID: ")
            for book in books:
                if book.get_book_id() == book_id:
                    if book.is_issued():
                        print("Book is already issued.")
                    else:
                        book.issue()
                        print("Book issued successfully.")
                    break
            else:
                print("Book not found.")
        case "4":
            book_id = input("Enter Book ID: ")
            for book in books:
                if book.get_book_id() == book_id:
                    if book.is_issued():
                        book.return_book()
                        print("Book returned successfully.")
                    else:
                        print("Book is already available.")
                    break
            else:
                print("Book not found.")
        case "5":
            print("\n===== AVAILABLE BOOKS =====")
            for book in books:
                if not book.is_issued():
                    book.display()
        case "6":
            manager = FileManager()
            manager.save(books)
        case "7":
            print("Thank you!")
            break
        case _:
            print("Invalid choice.")