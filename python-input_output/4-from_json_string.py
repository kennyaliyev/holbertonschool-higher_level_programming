#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string."""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        object: The Python object corresponding to the JSON string.
    """
    return json.loads(my_str)
