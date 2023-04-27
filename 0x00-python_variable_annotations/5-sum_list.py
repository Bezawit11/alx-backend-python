#!/usr/bin/env python3
"""a type-annotated function sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum as a float"""
    sum = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum
