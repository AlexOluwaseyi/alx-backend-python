#!/usr/bin/env python3

"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine that will
execute async_comprehension four times in
parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds,
explain it to yourself.

Explanation:
1.  Module async_generator loops 10 times, and wait for 1 seconds each time
    and yields the a random number. Making a total of 10 seconds wait
2.  Module async_comprehension uses module above, and that returns the 10
    numbers yielded by async_generator. This takes as much time as
    async_generator module.
3.  Module measure_runtime runs 4 instances of async_comprehension in
    parallel. That means each instance takes 10 seconds and all instances,
    run simulteneously, run for 10 seconds as well. Rather than 40 seconds.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.
    Measure time using time module
    Return elapsed_time
    """
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
