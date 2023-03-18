#!/usr/bin/python3

def weight_average(my_list=[]):
    '''returns the weighted average of all integers tuple'''

    if not my_list:
        return (0)

    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight
    
    weighted_average = total_weighted-score / total_weight

    return (weighted_average)
