#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """ Prints 'My name is <first_name> <last_name>.

    Args:
        first_name(str) = First name printed
        last_name(str) = Second name printed

    Raises:
        TypeError: if first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
