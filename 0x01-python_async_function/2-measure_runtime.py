#!/usr/bin/env python3
"""measure the run time"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """mesure the total execute time"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    last_time = time.perf_counter()
    total_time = last_time - start_time
    return total_time / n
