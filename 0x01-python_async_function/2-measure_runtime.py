#!/usr/bin/env python3
"""measure_time function with integers n and max_delay as arguments"""

import asyncio, random, time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """measures the total execution time for wait_n(n, max_delay), 
    and returns total_time
    """
    sum = 0
    l = asyncio.run(wait_n(n, max_delay))
    for i in l:
        sum += i
    return sum
