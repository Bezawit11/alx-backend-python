#!/usr/bin/env python3
"""asynchronous coroutine"""


import asyncio, random


async def wait_random(max_delay=10):
    """ waits for a random delay between 0 and max_delay"""
    a = random.uniform(0, flaot(max_delay + 1))
    await asyncio.sleep(a)
    return a
