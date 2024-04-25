#!/usr/bin/env python3
""" asynchronous routines in Python """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ takes n and max_delay and spawn wait_random n times """
    list_rndm = []
    for i in range(n):
        list_rndm.append(await wait_random(max_delay))
    return sorted(list_rndm)