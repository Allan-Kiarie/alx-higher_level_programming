#!/usr/bin/python3
# base.py
"""Defines a class Base."""
import json
import csv

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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string(str): string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary(dict): key/value pairs
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2)
        else:
            raise ValueError("Invalid class name")

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from JSON strings."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as jfile:
                jdata = jfile.read()
                list_dicts = Base.from_json_string(jdata)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a file.

        Args:
            list_objs(list): list of instances of a class.
        """
        filename = cls.__name__ + '.csv'

        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
                for obj in list_objs:
                    csvwriter.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of class instances from a csv file."""
        filename = cls.__name__ + '.csv'

        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                csvreader = csv.DictReader(csvfile, fieldnames=fields)
                list_dicts = [dict([key, int(value)] for
                                   key, value in d.items())
                                   for d in csvreader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
                return []
