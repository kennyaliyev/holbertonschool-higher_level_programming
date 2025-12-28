#!/usr/bin/python3
"""This module provides a function to check indirect inheritance."""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.
    Direct instances of a_class return False.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj inherits from a_class (not direct instance).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
