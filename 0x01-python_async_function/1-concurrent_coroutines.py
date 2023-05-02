#!/usr/bin/env python3
"""an async routine"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await wait_random(max_delay)
        lm.append(a)
    return lm
