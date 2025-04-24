#!/usr/bin/env python3
"""
This module contains a single asynchronous coroutine function `wait_random`.
The function generates a random delay and waits for that duration asynchronously.
"""
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
