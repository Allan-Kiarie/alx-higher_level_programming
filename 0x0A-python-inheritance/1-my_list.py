#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
