#!/usr/bin/env python3

"""
add type annotations to the function
Hint: look into TypeVar
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Annotated function that safely gets a value from a dictionary,
    returning a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
