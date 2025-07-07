#!/usr/bin/env python3
""" python async comprehension"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes async_comprehension 4 times in parallel and measures
    the total runtime and return it """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range (4)))
    end_time = asyncio.get_event_loop().time()
    time = end_time - start_time
    return time
