#!/usr/bin/env python3
"""Task 0: Abstract Animal class with Dog and Cat subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes.

        Must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """Dog subclass of Animal."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
