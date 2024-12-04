#!/usr/bin/env python3
""" variable annotations in Python """
from typing import List
""" import List to precise what is inside of the list"""


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    return sum(mxd_lst)
