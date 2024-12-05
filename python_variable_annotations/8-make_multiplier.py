#!/usr/bin/env python3
""" variable annotations in Python """
from typing import Callable
""" import Callable to precise that make_multiplier
will return a function """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier and returns a function that
    multiplies a float by multiplier """
    def multiplier_func(m: float) -> float:
        """ defines m float and multiplies a float by multiplier """
        return m * multiplier
    return multiplier_func
