#!/usr/bin/env python3
"""
This module defines an asynchronous function that waits for
a random delay between 0 and max_delay seconds, then returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random number of seconds between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
