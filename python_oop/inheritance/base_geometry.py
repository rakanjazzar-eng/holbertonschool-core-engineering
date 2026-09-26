#!/usr/bin/env python3
"""
This module defines the BaseGeometry class for geometric operations.
"""


class BaseGeometry:
    """A foundational class for geometric shapes."""

    def area(self):
        """
        Raise an Exception indicating that area calculation is not implemented.

        Raises:
            Exception: Always raises with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
