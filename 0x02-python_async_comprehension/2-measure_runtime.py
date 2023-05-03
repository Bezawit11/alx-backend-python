#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure the total runtime and return it"""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    elapsed = time.time() - start
    return elapsed
