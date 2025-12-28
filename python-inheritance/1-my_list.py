#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """A subclass of list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order.

        Does not modify the original list.
        """
        print(sorted(self))
