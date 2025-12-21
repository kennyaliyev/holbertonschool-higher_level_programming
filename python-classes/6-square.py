#!/usr/bin/python3
"""This module defines a Square class with position support."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square with size and position.

        Args:
            size (int): Side length. Must be non-negative integer.
            position (tuple): (x, y) offset. Must be 2 non-negative integers.
        Raises:
            TypeError: If size not int, or position invalid.
            ValueError: If size < 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position with validation.

        Args:
            value (tuple): Must be tuple of 2 non-negative integers.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with '#' at given position.

        Uses spaces for horizontal offset and newlines for vertical offset.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1] blank lines)
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
