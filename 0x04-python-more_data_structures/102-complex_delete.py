#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    '''deletes keys with a specific value in a dictionary'''

    keys_del = [k for (k, v) in a_dictionary.items() if v == value]

    for key in keys_del:
        del a_dictionary[key]

    return (a_dictionary)
