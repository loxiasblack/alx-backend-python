#!/usr/bin/env python3
"""return the right annotation"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a list of tuple with sequence and int"""
    return [(i, len(i)) for i in lst]
