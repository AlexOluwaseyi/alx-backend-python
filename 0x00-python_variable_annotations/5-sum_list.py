#!/usr/bin/env python3

"""
a type-annotated function sum_list which
takes a list input_list of floats as
argument and returns their sum as a float.
"""

from typing import List
Vector = List[float]


def sum_list(input_list: Vector) -> float:
    """
    Type annotated function tking a list of float
    to sum up and return a float
    """
    sub_sum: float = 0
    for value in input_list:
        sub_sum += value

    return sub_sum
