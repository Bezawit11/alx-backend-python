#!/usr/bin/env python3
"""äsyncio tasks"""

import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await task_wait_random(max_delay)
        lm.append(a)
    return lm
