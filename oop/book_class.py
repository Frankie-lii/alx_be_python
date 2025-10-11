#!/usr/bin/env python3
# book_class.py

class Book:
    """A class to represent a Book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor that initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
