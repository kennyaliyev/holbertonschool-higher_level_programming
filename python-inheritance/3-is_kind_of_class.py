#!/usr/bin/python3
"""This module provides a function to check class or inheritance match."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or inherits from, a_class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is instance of a_class or its subclass.
    """
    return isinstance(obj, a_class)
