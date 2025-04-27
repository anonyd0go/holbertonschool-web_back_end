#!/usr/bin/env python3
"""
Module that contains an async routine wait_n that spawns wait_random n times
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds
  
    Returns:
        List[float]: List of all the delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
