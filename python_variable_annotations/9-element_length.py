#!/usr/bin/env python3
""" variable annotations in Python """
from typing import Tuple, Union
""" import List to precise what is inside of the list """

def element_length(lst):
    return [(i, len(i)) for i in lst]
