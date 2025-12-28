#!/usr/bin/python3
"""Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    It uses the parent class's implementation for area and string representation,
    since width and height are equal.
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
