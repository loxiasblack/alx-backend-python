#!/usr/bin/env python3
"""anotate with typing"""

from typing import Tuple, Union

Vector = Tuple[str, float]


def to_kv(k: str, v: Union[int, float]) -> Vector:
    """return tuple"""
    return (k, v * v)
