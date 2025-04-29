#!/usr/bin/env python3
"""
This module measures the total runtime for executing
four async comprehensions concurrently.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension four times in parallel
    and returns the total elapsed time.
    """
    start = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end = time.perf_counter()

    return end - start
