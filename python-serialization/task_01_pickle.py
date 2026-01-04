#!/usr/bin/env python3
"""CustomObject class with pickle-based serialization support."""

import pickle


class CustomObject:
    """A custom class that supports pickling and unpickling."""

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file using pickle.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from a pickle file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject or None: The deserialized object, or None if failed.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, Exception):
            return None
