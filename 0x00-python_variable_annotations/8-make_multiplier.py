#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function"""
    def multiplier_func(n: float) -> float:
        """return mult"""
        return (n * multiplier)
    return (multiplier_func)
