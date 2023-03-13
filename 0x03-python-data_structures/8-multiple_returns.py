#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character'''

    if sentence:
        result = [len(sentence), sentence[0]]
    else:
        result = [len(sentence), None]

    return tuple(result)
