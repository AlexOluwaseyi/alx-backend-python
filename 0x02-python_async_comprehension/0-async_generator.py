#!/usr/bin/env python3

"""
0. Async Generator
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    A co-routine that takes no argument
    loops 10 times, waits 1 sec and yields
    a random number between 0 & 10"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
