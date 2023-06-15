#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
