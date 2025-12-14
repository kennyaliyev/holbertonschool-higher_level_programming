#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.
    Args:
        my_list (list): List of any type.
        x (int): Number of elements to access.
    Returns:
        int: Number of integers printed.
    Note:
        - Non-integers are skipped silently.
        - If x > len(my_list), IndexError is raised (not caught).
        - Uses '{:d}'.format() for printing.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
