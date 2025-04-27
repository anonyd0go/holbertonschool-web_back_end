#!/usr/bin/env python3
"""
Module that contains an async routine called task_wait_n
that spawns task_wait_random n times
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay in seconds

    Returns:
        List[float]: List of all the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
