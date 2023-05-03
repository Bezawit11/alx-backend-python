#!/usr/bin/env python3
""""""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    elapsed = time.time() - start
    return elapsed
