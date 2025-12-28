#!/usr/bin/env python3
"""Task 5: Dragon using SwimMixin and FlyMixin."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print a generic swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print a generic flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""

    def roar(self):
        """Print a dragon-specific roar message."""
        print("The dragon roars!")
