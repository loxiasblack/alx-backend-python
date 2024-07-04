#!/usr/bin/env python3
"""annotation with multiplier"""
from typing import Callable

Vector = Callable[[float], float]


def make_multiplier(multiplier: float) -> Vector:
    """make multiplier function"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
