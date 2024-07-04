#!/usr/bin/env python3
"""return the right annotation"""
from typing import Sequence, Tuple, List


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """a list of tuple with sequence and int"""
    return [(i, len(i)) for i in lst]
