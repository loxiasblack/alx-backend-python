#!/usr/bin/env python3
"""Run the time for four parallel"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """calcule the time elaspsed with calling 4 times the
    imported function"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - start_time
    return elapsed
