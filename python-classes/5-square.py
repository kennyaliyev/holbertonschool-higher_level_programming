#!/usr/bin/python3
"""This module defines a Square class with printing capability."""


class Square:
    """Represents a square with size validation and printing."""

    def __init__(self, size=0):
        """Initializes the square with optional size (default: 0).

        Args:
            size (int): The size of the square. Must be a non-negative integer.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation.

        Args:
            value (int): New size. Must be non-negative integer.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
