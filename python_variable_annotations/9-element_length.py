#!/usr/bin/env python3
"""
This module contains a function that returns the length of each element
in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element
    from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
