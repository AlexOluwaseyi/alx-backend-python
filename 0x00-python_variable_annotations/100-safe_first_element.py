#!/usr/bin/env python3

"""
a type-annotated function element_length
that takes an iterable of Sequence as argument
and returns a list of tuple of sequences and integer."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck-typed annotations:"""
    if lst:
        return lst[0]
    else:
        return None
