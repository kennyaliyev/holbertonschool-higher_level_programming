#!/usr/bin/python3
"""Adds all command-line arguments to a list and saves to add_item.json."""

import sys

# Safely import functions from files with numbers
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list or start with empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
