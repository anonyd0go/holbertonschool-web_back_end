#!/usr/bin/env python3
"""
Module that creates an asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task

    Args:
        max_delay (int): Maximum delay in seconds

    Returns:
        asyncio.Task: Task that will execute wait_random with the max_delay
    """
    # Create and return a Task that will execute wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task
