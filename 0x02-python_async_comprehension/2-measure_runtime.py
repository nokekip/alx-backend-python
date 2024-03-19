#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension four times in parallel using
asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return end_time - start
