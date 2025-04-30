#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine function `async_comprehension`.
The function collects 10 random numbers from an asynchronous generator
using an async comprehension.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random floating-point numbers
    from the `async_generator` using an async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [x async for x in async_generator()]
