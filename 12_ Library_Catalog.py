# 12-: Library Catalog
#
# Create Python classes for a library catalog system. The classes you need to create are:

# Book: Represents a book with attributes such as title, author, ISBN, and availability status.
# Library: Represents the library, which contains a collection of books and can perform operations like adding a book, removing a book, and checking out a book.
# Here are the specifications for each class:
#
# Book Class:

# Attributes:

# Title (string)
# Author (string)
# ISBN (string)
# Available (boolean, initially set to True)
# Methods:
#
# __init__(self, title: str, author: str, isbn: str): Initialize a book with a title, author, and ISBN. Set the availability to True initially.
# get_title(self) -> str: Return the title of the book.
# get_author(self) -> str: Return the author of the book.
# get_isbn(self) -> str: Return the ISBN of the book.
# is_available(self) -> bool: Return True if the book is available; otherwise, return False.
# checkout(self): Set the availability of the book to False to indicate that it's checked out.
# checkin(self): Set the availability of the book to True to indicate that it's checked in.
# Library Class:
#
# Attributes:
#
# Books (a list to store Book objects)
# Methods:
#
# __init__(self): Initialize the library with an empty list of books.
# add_book(self, book: Book): Add a book to the library's collection of books.
# remove_book(self, isbn: str): Remove a book from the library's collection based on its ISBN.
# checkout_book(self, isbn: str) -> bool: Attempt to check out a book with the given ISBN. If successful, return True; otherwise, return False.
# checkin_book(self, isbn: str) -> bool: Attempt to check in a book with the given ISBN. If successful, return True; otherwise, return False.
# list_books(self) -> List[str]: Return a list of titles of all available books in the library.
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def get_title(self):
        """Return the title of the book."""
        return f'Title: {self.title}'

    def get_author(self):
        """Return the author of the book."""
        return f'Author: {self.author}'

    def get_isbn(self):
        """Return the ISBN of the book."""
        return f'ISBN: {self.ISBN}'

    def is_available(self):
        """ Return True if the book is available; otherwise, return False."""
        return self.available

    def checkout(self):
        """Set the availability of the book to False to indicate that it's checked out."""
        self.available = False

    def checkin(self):
        """Set the availability of the book to True to indicate that it's checked in."""
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library's collection of books."""
        self.books.append(book)
        print('Book has been added to Library Successfully.!')

    def remove_book(self, isbn):
        """Remove a book from the library's collection based on its ISBN."""
        for book in self.books:
            if book.ISBN == isbn:
                self.books.remove(book)
                print(f'Your book: {isbn} remove successfully.!')
                return
        print(f'Book: {isbn} Does not exist.!')

    def checkout_book(self, isbn):
        """Attempt to check out a book with the given ISBN. If successful, return True; otherwise, return False."""
        for book in self.books:
            if book.ISBN == isbn and book.is_available():
                book.checkout()
                return True
        return False

    def checkin_book(self, isbn):
        """Attempt to check in a book with the given ISBN. If successful, return True; otherwise, return False."""
        for book in self.books:
            if book.ISBN == isbn and not book.is_available():
                book.checkin()
                return True
        return False

    def list_books(self):
        """ Return a list of titles of all available books in the library."""
        available_books = [book.get_title() for book in self.books if book.is_available()]
        return available_books


book1 = Book("Mom's Fucker", 'James valley', '1212-34-456')
book2 = Book('The Whole', 'Naim Shaikh', '1234-89-99')

# print(book1.get_title())
# # print(book2.get_title())
# print(book1.get_author())
# print(book1.get_isbn())


lib1 = Library()

# add books in library.
lib1.add_book(book1)
lib1.add_book(book2)

# lib1.remove_book('1212-34-456')

# print(lib1.checkout_book('1234-89-99'))

print(lib1.checkin_book('123499'))

print(lib1.list_books())
