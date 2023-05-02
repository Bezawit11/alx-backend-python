#!/usr/bin/env python3
"""an async routine"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await wait_random(max_delay)
        lm.append(a)
    return lm
