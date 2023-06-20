#!/usr/bin/python3
# base.py
"""Defines a class Base."""
import json


class Base:
    """A representation of the object base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the object Base.

        Args:
            id(int): identify of the class Base.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries(dict): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
