#!/usr/bin/env python3

"""
a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""

from typing import List, Union

MixedList = List[Union[int, float]]


def sum_mixed_list(mxd_list: MixedList) -> float:
    """
    Type annotated function tking a list of float
    to sum up and return a float
    """
    sub_sum: float = 0
    for value in mxd_list:
        sub_sum += value

    return sub_sum
