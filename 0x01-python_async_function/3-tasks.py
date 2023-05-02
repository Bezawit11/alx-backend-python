#!/usr/bin/env python3
"""tasks in asyncio """

import asyncio, random, time
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay):
    """returns a task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
