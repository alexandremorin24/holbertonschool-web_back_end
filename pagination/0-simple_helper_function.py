#!/usr/bin/env python3
"""
This module defines a helper function for pagination:
it calculates start and end indexes based on page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of (start_index, end_index) to paginate data."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
