#!/usr/bin/env python3
"""
This module contains a function that returns a tuple with a string and
the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing a string and the square of a number."""
    return (k, float(v ** 2))
