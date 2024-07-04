#!/usr/bin/env python3
"""
retrun floor of a float
"""


def floor(n: float) -> int:
    """with anotation round the float"""
    if (n - int(n)) <= 0.5:
        return int(n)
    else:
        return int(n) + 1
