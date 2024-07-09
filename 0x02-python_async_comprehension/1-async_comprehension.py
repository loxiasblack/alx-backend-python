#!/usr/bin/env python3
"""Async Comprehension"""
import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Generator[float, None, None]]:
    """collect 10 random number"""
    results = [i async for i in async_generator()]
    return results
