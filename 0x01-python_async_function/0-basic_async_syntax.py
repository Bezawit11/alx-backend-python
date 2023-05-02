#!/usr/bin/env python3
"""asynchronous coroutine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay"""
    a = random.uniform(0, max_delay + 1)
    await asyncio.sleep(a)
    return a
