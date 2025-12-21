#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size attribute."""
    def __init__(self, size):
        """Initializes the square with a given size.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
