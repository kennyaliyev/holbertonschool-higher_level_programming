#!/usr/bin/python3
"""This module defines a Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    Since a square is a rectangle with equal width and height,
    it uses the parent class's implementation for area and string representation.
    """

    def __init__(self, size):
        """Initializes a Square with validated size.

        Args:
            size (int): The side length of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
