#!/usr/bin/env python3
"""
This module defines a Square class with a private instance attribute size.
"""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
