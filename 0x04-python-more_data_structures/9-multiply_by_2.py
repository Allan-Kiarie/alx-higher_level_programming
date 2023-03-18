#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''returns a new dictionary with all values multiplied by 2'''

    newDict = {}

    for key, value in a_dictionary.items():
        newDict = value * 2

    return (newDict)
