#!/usr/bin/env python3
"""tasks in asyncio """

import asyncio
import random
import time
wait_random = __import__('0-basic_async_syntax').wait_random

<<<<<<< HEAD

def task_wait_random(max_delay):
=======
def task_wait_random(max_delay: int) -> asyncio.Task:
>>>>>>> c7e30f4cd1a00498d7ae29ceba9552839797cba3
    """returns a task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
