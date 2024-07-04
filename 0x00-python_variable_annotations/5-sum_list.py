#!/usr/bin/env python3
"""
return float the sum of the list
"""


def sum_list(input_list: list) -> float:
    """with anotaion return the sum of list"""
    sum = 0
    for i in input_list:
        sum += i
    return sum
