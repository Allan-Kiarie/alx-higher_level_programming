#!/usr/bin/python3

def weight_average(my_list=[]):
    '''returns the weighted average of all integers tuple'''

    if not my_list:
        return (0)

    t_score = 0
    t_weight = 0

    for (score, weight) in my_list:
        t_score += score * weight
        t_weight += weight

    return(t_score / t_weight)
