#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine function `measure_runtime`.
The function measures the total runtime of executing `async_comprehension`
four times in parallel using `asyncio.gather`.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Asynchronous coroutine that measures the runtime of executing
    `async_comprehension` four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
        )

    end = time.time()

    return end - start
