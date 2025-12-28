#!/usr/bin/python3
"""This module defines a complete Rectangle class with area and string rep."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): Private width attribute.
        __height (int): Private height attribute.
    """

    def __init__(self, width, height):
        """Initializes a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Format: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
