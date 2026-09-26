#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in list.
"""


class VerboseList(list):
    """A custom list class that prints notifications when modified."""

    def append(self, item):
        """Add an item to the end of the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list by appending elements
        from iterable and print a message."""
        items = list(iterable)
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove first occurrence of item
        and print a message before doing so."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index
        (default last) and print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
