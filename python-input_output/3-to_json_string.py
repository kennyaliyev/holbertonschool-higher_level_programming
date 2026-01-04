#!/usr/bin/python3
"""Returns the JSON representation of an object (string)."""

import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object.

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
