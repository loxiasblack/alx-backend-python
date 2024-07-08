#!/usr/bin/env python3
"""asyncio to return a random sleep"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynochronous coroutine
    Args: max_delay (int): max of waiting
    Returns: float number
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
