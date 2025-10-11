#!/usr/bin/env python3

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Multiplies two numbers and prints class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
