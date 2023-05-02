#!/usr/bin/env python3
"""asyncio tasks"""


import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await task_wait_random(max_delay)
        lm.append(a)
    return lm
