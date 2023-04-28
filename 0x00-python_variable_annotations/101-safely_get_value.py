#!/usr/bin/env python3
"""duck-typed annotations"""


from typing import Sequence, Any, Union, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None] = None) -> Union[Any, TypeVar]:
    """duck-typed annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
