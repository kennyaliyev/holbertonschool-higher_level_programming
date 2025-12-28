#!/usr/bin/env python3
"""Task 3: CountedIterator that tracks how many items have been iterated."""


class CountedIterator:
    """An iterator that counts the number of items retrieved."""

    def __init__(self, iterable):
        """Initialize with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, etc.).
        """
        self.iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        """Fetch next item and increment counter."""
        item = next(self.iterator)
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self._count
