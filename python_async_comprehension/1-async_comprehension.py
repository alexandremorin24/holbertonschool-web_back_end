#!/usr/bin/env python3
"""
This module defines an async comprehension function
that collects 10 random numbers from async_generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random floats asynchronously from async_generator
    and return them as a list.
    """
    return [i async for i in async_generator()]
