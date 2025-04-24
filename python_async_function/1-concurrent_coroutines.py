#!/usr/bin/env python3
"""
This module defines an async routine that runs multiple coroutines concurrently
and returns a list of their results, in the order they completed.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay and returns a list of delays
    in ascending order (based on completion time).
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        delays.append(result)

    return delays
