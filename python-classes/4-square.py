#!/usr/bin/python3
"""This module defines a Square class with size property."""


class Square:
    """Represents a square with a validated size property."""

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
        """Retrieves the size of the square.

        Returns:
            int: The private size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size. Must be a non-negative integer.
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
        """Computes and returns the current area of the square.

        Returns:
            int: Area = size * size.
        """
        return self.__size * self.__size
