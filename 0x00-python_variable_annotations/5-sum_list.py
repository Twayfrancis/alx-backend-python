#!/usr/bin/env python3
"""type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes single arg input_list returns sum of all num in list"""
    return (sum(input_list))
