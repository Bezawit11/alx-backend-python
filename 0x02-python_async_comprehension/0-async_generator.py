#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def async_generator() -> float:
    """loops 10 times, eachtime asynchronously wait 1 sec, yield a random num"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
