#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle.

    It overrides the string representation to show [Square] instead of [Rectangle].
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

    def __str__(self):
        """Returns the string representation of the square.

        Format: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
