#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''

    mykeys = list(a_dictionary.keys())
    mykeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in mykeys}

    return (sorted_dict)
