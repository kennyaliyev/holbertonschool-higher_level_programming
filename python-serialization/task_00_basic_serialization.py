#!/usr/bin/env python3
"""Basic serialization module for JSON file I/O."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
