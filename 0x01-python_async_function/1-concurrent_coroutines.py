#!/usr/bin/env python3
"""an async routine"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all the delays"""
    lm = []
    tem = 0
    for i in range(n):
        a = await wait_random(max_delay)
        lm.append(a)
    for i in range(0, len(lm)):
        for j in range(0, len(lm)):
            if lm[i] < lm[j]:
                tem = lm[i]
                lm[i] = lm[j]
                lm[j] = tem
    return lm
