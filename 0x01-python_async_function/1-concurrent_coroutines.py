#!/usr/bin/env python3
"""multiples coroutines at the same time"""
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait n times"""
    new_list = []
    for _ in range(n):
        r = await wait_random(max_delay)
        new_list.append(r)
    return new_list
