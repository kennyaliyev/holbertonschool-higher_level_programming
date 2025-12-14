#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (each integer only once).

    Args:
        my_list (list): List of integers (may contain duplicates).

    Returns:
        int: Sum of all unique integers.
    """
    unique_set = set()
    for num in my_list:
        unique_set.add(num)
    return sum(unique_set)
