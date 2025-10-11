#!/usr/bin/env python3
# library_system.py

class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        """Initialize common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a generic book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize EBook attributes, including those from the Book class."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes, including those from the Book class."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books."""

    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
