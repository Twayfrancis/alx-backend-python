#!/usr/bin/env python3
"""a coroutine called async_comprehension that takes no arguments"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
        coroutine will collect 10 random numbers using
        async comprehensing over async_generator,
        then return the 10 random numbers.
    """
    done_tasks = [i async for i in async_generator()]
    return done_tasks
