#!/usr/bin/env python3

"""
a type-annotated function element_length
that takes an iterable of Sequence as argument
and returns a list of tuple of sequences and integer."""

from typing import List, Tuple, Sequence, Iterable

output = List[Tuple[Sequence, int]]
iterable = Iterable[Sequence]


def element_length(lst: iterable) -> output:
    return [(i, len(i)) for i in lst]
