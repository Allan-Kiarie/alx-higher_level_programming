#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''Adds two tupples.
    The 1st element is the addition of the 1st element of each argument
    The 2nd element is the addition of the 2nd element of each argument
    '''
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    result = []
    for i in range(2):
        result.append(tuple_a[i] + tuple_b[i])
    return tuple(result)
