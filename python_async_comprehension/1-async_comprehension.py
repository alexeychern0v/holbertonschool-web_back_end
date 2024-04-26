#!/usr/bin/env python3
""" coroutine """
import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ coroutine collects 10 random numbers using an async comprehensing and returns the 10 random numbers """
    random_numbers = [rndm async for rndm in async_generator()]
    return random_numbers