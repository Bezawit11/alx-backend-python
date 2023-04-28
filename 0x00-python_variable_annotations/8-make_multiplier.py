#!/usr/bin/env python3
""" """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def mul(m: float) -> float:
        """the returned function"""
        return m * multiplier
    return mul
