#!/usr/bin/env python3
""" coroutine async_generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ coroutine loops 10 times, yields a random number between 0 and 10 """
    for task_zero in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)