#!/usr/bin/python3
# square.py
"""Defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of the object square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initalizes a new class Square.

        Args:
            size(int): size of the Square
            x(int): x-coordinate of the Square
            y(int): y-coordinate of the Square
            id(int): identity of the Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/access the attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the new class Square.

        Args:
            *args: Update attribute values
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            **kwargs(dict): key/value (keyworded arguments)
                - Must be skipped if *args exists and is not empty
                - Each key represents an attribute to the instance
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary representation of class Square."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """Returns print() and str() representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
