#!/usr/bin/env python3
"""Annotated function"""


from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotated python function"""
    return [(i, len(i)) for i in lst]
