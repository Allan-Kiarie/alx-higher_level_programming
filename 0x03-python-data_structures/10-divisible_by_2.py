#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list'''

    result = [x for x in my_list]

    for i in range(len(result)):
        if result[i] % 2 == 0:
            result[i] = True
        else:
            result[i] = False
    return (result)
