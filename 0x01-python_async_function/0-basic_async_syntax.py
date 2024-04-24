#!/usr/bin/env python3

"""
A python module for an asynchronous coroutine
0. The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function definition for  an asynchronous coroutine that takes in
    an integer argument (max_delay, with a default value of 10) named
    wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """
    rand_wait: float = random.random() * max_delay
    await asyncio.sleep(rand_wait)
    return rand_wait
