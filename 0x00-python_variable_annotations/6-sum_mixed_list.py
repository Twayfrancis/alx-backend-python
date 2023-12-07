#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """takes input_list and returns their sum as float"""
    return sum(mxd_lst)
