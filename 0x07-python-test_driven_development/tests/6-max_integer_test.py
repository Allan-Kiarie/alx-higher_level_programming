#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Performs unittests for max_integer([..])."""

    def test_sorted_list(self):
        """Test a sorted list of integers."""
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unsorted_list(self):
        """Tests unsorted list of integer."""
        my_list = [1, 3, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_begin_at_max(self):
        """Test a list that starts with max value"""
        my_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(my_list), 4)

    def test_empty_list(self):
        """Test an empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_single_elem(self):
        """Test single element"""
        my_list = [4]
        self.assertEqual(max_integer(my_list), 4)

    def test_floats(self):
        """Tests floats"""
        my_list = [1.25, 2.85, 9.45, 0.52]
        self.assertEqual(max_integer(my_list), 9.45)

    def test_both_ints_floats(self):
        """Tests both floats and integers"""
        my_list = [5, 6.9, 6, 2]
        self.assertEqual(max_integer(my_list), 6.9)

    def test_string(self):
        """Tests a string"""
        string = "Kiarie"
        self.assertEqual(max_integer(string), 'r')

    def test_list_strings(self):
        """Test a list of strings"""
        my_strings = ["Money", "World", "Go", "Round"]
        self.assertEqual(max_integer(my_strings), "World")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)
