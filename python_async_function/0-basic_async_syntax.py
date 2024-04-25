#!/usr/bin/env python3
""" asynchronous routines in Python """
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay and returns it """
    rndm_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rndm_delay)
    return rndm_delay