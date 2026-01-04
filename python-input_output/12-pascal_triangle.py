#!/usr/bin/python3
"""Generates Pascal's Triangle up to n rows."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start each row with [1]
        row = [1]
        if i > 0:
            # Add middle elements by summing adjacent values from previous row
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            # End row with [1] (except for first row)
            row.append(1)
        triangle.append(row)

    return triangle
