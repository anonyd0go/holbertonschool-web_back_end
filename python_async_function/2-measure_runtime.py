#!/usr/bin/env python3
"""
Module that measures the runtime of wait_n coroutine
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds

    Returns:
        float: Average execution time per coroutine
    """
    async def _measure():
        start_time = time.time()

        await wait_n(n, max_delay)

        end_time = time.time()
        total_time = end_time - start_time

        return total_time / n

    # Run the async function inside this sync function
    return asyncio.run(_measure())
