#!/usr/bin/env python3
""" python async comprehension"""
import asyncio
import random

async def async_generator():
    """ coroutine loops 10 times, each time asynchronously wait 1 second
    then yield a random number between 0 and 10 """
    list = []
    for _ in range(10):
        await asyncio.sleep(1)
        list.append(random.uniform(0, 10))
    return list
