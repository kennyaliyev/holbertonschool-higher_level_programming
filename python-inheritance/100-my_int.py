#!/usr/bin/python3
"""Module for MyInt class that inverts == and != operators."""


class MyInt(int):
    """A rebel integer class that inverts == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
