#!/usr/bin/env python3
"""annotation union list"""
from typing import List, Union

Vector = List[Union[int, float]]


def sum_mixed_list(mxd_lst: Vector) -> float:
    """return float sum"""
    return sum(mxd_lst)
