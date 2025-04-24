#!/usr/bin/env python3
"""
This module defines a function that measures the average runtime
of an asynchronous call to wait_n with n concurrent coroutines.
"""

import asyncio
import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total time taken to run wait_n(n, max_delay),
    and returns the average time per coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    average_time = total_time / n
    return average_time
