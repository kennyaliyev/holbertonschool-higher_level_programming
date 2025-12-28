#!/usr/bin/env python3
"""Task 2: VerboseList that prints notifications on modifications."""


class VerboseList(list):
    """A list subclass that prints notifications for append, extend, remove, pop."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification with count."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a notification before removal."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification before removal."""
        item = self[index]  # Get item before popping
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
