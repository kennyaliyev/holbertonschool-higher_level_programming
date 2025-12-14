#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one of the two sets.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: Symmetric difference of set_1 and set_2.
    """
    return set_1 ^ set_2
