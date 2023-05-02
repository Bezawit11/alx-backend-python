#!/usr/bin/env python3
"""measure_time function with integers n and max_delay as arguments"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


<<<<<<< HEAD
def measure_time(n, max_delay):
    """measures the total execution time for wait_n(n, max_delay),
=======
def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay), 
>>>>>>> c7e30f4cd1a00498d7ae29ceba9552839797cba3
    and returns total_time
    """
    sum = 0
    lm = asyncio.run(wait_n(n, max_delay))
    for i in lm:
        sum += i
    return sum
