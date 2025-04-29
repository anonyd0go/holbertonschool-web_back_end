#!/usr/bin/env python3
"""
This module defines an asynchronous generator function `async_generator`.
The function yields random floating-point numbers asynchronously.
"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronous generator that yields 10 random floating-point numbers
    between 0 and 10, with a 1-second delay between each.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
