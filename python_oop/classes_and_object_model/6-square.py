#!/usr/bin/env python3
"""
This module defines a Square class with size and position attributes,
getters/setters, area calculation, printing capabilities,
and string representation.
"""


class Square:
    """Defines a square with private size and position attributes,

    methods for area, print, and string representation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's side (default 0).
            position (tuple): The (x, y) offset position for
            printing (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get the current position of the square.

        Returns:
            tuple: The (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The (x, y) tuple position.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character and position in stdout."""
        print(self.__str__())

    def __str__(self):
        """Return the string representation of the square for printing.

        Returns:
            str: Formatted square representation with
            horizontal and vertical offsets.
        """
        if self.__size == 0:
            return ""

        square_lines = []
        for _ in range(self.__position[1]):
            square_lines.append("")

        for _ in range(self.__size):
            square_lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(square_lines)
