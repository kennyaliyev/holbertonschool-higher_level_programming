#!/usr/bin/python3
"""Student class with serialization, filtering, and reloading from JSON."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the Student.
        """
        if (
            isinstance(attrs, list) and
            all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
