#!/usr/bin/env python3
"""
retrun floor of a float
"""


def floor(n: float) -> int:
    """with anotation round the float"""
    return int(n) if n >= 0 else int(n) - 1
