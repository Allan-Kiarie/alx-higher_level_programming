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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries(dict): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs(list): a list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"

        with open(file_name, 'w') as jfile:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_dicts)
            jfile.write(json_str)
