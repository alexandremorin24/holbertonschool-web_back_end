#!/usr/bin/env python3
"""
This module defines a function that schedules and runs
multiple asynchronous tasks using task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Launches n tasks using task_wait_random and returns the delays
    in the order in which the tasks are completed (not in order of launch).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
