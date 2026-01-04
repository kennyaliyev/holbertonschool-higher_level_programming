#!/usr/bin/python3
"""Writes a string to a text file (UTF-8) and returns character count."""


def write_file(filename="", text=""):
    """
    Writes a string to file (UTF-8) and returns  number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
