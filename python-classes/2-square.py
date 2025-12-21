#!/usr/bin/python3
"""This module defines a Square class with size validation."""


class Square:
    """Represents a square with a validated private size attribute."""
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
