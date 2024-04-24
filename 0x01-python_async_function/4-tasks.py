#!/usr/bin/env python3

"""
Similar to wait_n
except task_wait_random is being called.
"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments (in this order): n and max_delay.
    Calls task_wait_random.
    """
    store: list = []
    for i in range(n):
        random_wait: float = await task_wait_random(max_delay)
        insert_index = 0
        while insert_index < len(store) and store[insert_index] <= random_wait:
            insert_index += 1
        store.insert(insert_index, random_wait)

    return store
