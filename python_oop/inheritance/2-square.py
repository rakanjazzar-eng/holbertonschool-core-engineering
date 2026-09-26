#!/usr/bin/env python3
"""
This module defines the Square class which inherits from Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, derived from Rectangle."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the sides of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return the string representation of the Square instance.

        Returns:
            str: Description formatted as [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
