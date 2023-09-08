# Problem: Book Library

# Create a Python class called Book that represents a book with the following attributes:

# (i).   Title
# (ii).  Author
# (iii). ISBN (International Standard Book Number)

# Implement a Library class that represents a library containing a collection of books.
# The Library class should have the following features:

# 1. Initialize an empty collection of books.
# 2. Implement a method to add a book to the library.
# 3. Implement a method to remove a book from the library.
# 4. Implement a method to search for a book by title and return its details (title, author, and ISBN).

class Book:
    def __init__(self, title, author, ISBN):
        self._title = title
        self._author = author
        self._ISBN = ISBN


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'Book has been successfully added.!')

    def remove_book(self, book_name):
        self.books.remove(book_name)
        print('Your book has been removed successfully.!')

    def search_book(self, title):
        for book in self.books:
            print(f'Title: {book._title}, Author: {book._author}, ISBN: {book._ISBN}')


book1 = Book("Dark Man", 'James villy', "90930-342-233")
lib1 = Library()
lib1.add_book(book1)
lib1.search_book('Dark Man')

book2 = Book('Creazy Dict', 'Herina van', '9034-22-34')
lib1.add_book(book2)
