#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by sorted keys (alphabetical order, case-sensitive).
    Args:
        a_dictionary (dict): The dictionary to print.
    Note:
        - Only top-level keys are sorted and printed.
        - Keys are assumed to be strings.
        - Values can be of any type.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
