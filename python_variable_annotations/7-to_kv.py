#!/usr/bin/env python3
""" variable annotations in Python """
from typing import Tuple, Union
""" import List to precise what is inside of the list """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments and returns a tuple
    The first element of the tuple is the string k
    The 2nd element is the square of v and should be annotated as a float
    """
    return (k, float(v**2))
