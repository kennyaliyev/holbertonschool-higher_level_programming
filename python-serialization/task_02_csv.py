#!/usr/bin/env python3
"""Converts CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON and saves it as 'data.json'.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
