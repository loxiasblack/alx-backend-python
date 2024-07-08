#!/usr/bin/env python3
"""asyncio to return a random sleep"""
import asyncio
import random


async def wait_random(max_delay=10):
    """random sleep"""
    s = random.uniform(0, max_delay)
    await asyncio.sleep(s)
    return s
