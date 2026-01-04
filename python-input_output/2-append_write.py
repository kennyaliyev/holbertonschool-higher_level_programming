#!/usr/bin/python3
"""Appends a string to  file (UTF-8) and returns number of chars added."""


def append_write(filename="", text=""):
    """
    Appends a string to  file and returns number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text to append. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
