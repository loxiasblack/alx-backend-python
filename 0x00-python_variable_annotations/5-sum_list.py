#!/usr/bin/env python3
"""typing list"""
from typing import List


Vector = List[float]


def sum_list(input_list: Vector) -> float:
    """with anotaion return the sum of list"""
    return sum(input_list)
