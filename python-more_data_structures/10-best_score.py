#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.
    Args:
        a_dictionary (dict or None): Dictionary with string keys and
                                     integer values.
    Returns:
        str or None: Key with highest value, or None if dictionary is
                     None/empty.
    """
    if not a_dictionary:
        return None
    best_key = None
    best_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
