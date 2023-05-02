#!/usr/bin/env python3
"""an async routine"""

<<<<<<< HEAD
import asyncio
import random
=======

import asyncio, random
from typing import List
>>>>>>> c7e30f4cd1a00498d7ae29ceba9552839797cba3
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all the delays"""
    lm = []
    for i in range(n):
        a = await wait_random(max_delay)
        lm.append(a)
    return lm
