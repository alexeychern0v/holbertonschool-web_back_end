#!/usr/bin/env python3
""" task_wait_n function was created with the specified prototype """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn task_wait_random n times with the specified max_delay """
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)


    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays