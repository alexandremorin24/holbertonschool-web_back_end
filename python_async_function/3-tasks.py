#!/usr/bin/env python3
"""
This module defines a function that creates an asyncio.Task
from the wait_random coroutine.
"""

import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object for the wait_random coroutine,
    already scheduled to run.
    """
    return asyncio.create_task(wait_random(max_delay))
