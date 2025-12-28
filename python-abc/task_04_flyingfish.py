#!/usr/bin/env python3
"""Task 4: FlyingFish using multiple inheritance from Fish and Bird."""


class Fish:
    """A base class representing a fish."""

    def swim(self):
        """Print a message about swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about fish habitat."""
        print("The fish lives in water")


class Bird:
    """A base class representing a bird."""

    def fly(self):
        """Print a message about flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class that inherits from both Fish and Bird."""

    def fly(self):
        """Override fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
