#!/usr/bin/env python3
"""
This module defines an Abstract Base Class Animal
and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound made by the animal."""
        pass


class Dog(Animal):
    """Class representing a dog, derived from Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat, derived from Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
