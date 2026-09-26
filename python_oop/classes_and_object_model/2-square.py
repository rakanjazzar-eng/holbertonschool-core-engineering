#!/usr/bin/env python3
"""
This module defines a Square class with size validation and a default value.
"""


class Square:
    """Defines a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's side (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
