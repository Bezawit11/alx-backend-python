#!/usr/bin/env python3
"""äsyncio tasks"""

<<<<<<< HEAD
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
=======

import asyncio, random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
>>>>>>> c7e30f4cd1a00498d7ae29ceba9552839797cba3
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await task_wait_random(max_delay)
        lm.append(a)
    return lm
