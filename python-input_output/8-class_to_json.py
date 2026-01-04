#!/usr/bin/python3
"""Returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's serializable attributes.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return obj.__dict__
