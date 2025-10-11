#!/usr/bin/env python3
# polymorphism_demo.py

import math

class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Raises an error to indicate subclasses must override this method."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        """Initialize circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
