#!/usr/bin/env python3
"""
This module defines SwimMixin, FlyMixin, and the Dragon class
that combines both mixins.
"""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, inheriting
    swimming and flying capabilities."""

    def roar(self):
        """Print roaring behavior specific to the Dragon."""
        print("The dragon roars!")
