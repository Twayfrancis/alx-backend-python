#!/usr/bin/env python3
"""
print three lists of float numbers which represent
the random delay time for each wait_random function call
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        print three lists of float numbers which represent
        the random delay time for each wait_random function call
        The delay time is between 0 and input argument (default is 10)
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    done_tasks = [await task for task in asyncio.as_completed(tasks)]
    return done_tasks
