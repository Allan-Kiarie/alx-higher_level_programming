#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''

    mykeys = list(a_dictionary.keys())
    mykeys.sort()

    for i in mykeys:
        print("{}: {}".format(i, a_dictionary[i]))
