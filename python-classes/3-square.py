#!/usr/bin/python3
"""This module defines a Square class with area computation."""


class Square:
    """Represents a square with validated size and area method."""
    def __init__(self, size=0):
        """Initializes the square with optional size (default: 0).
        Args:
            size (int): The size of the square. Must be a non-negative integer.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Computes and returns the current area of the square.
        Returns:
            int: Area = size * size.
        """
        return self.__size * self.__size
