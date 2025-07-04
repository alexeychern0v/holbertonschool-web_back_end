#!/usr/bin/env python3
""" variable annotations in Python """
from typing import Iterable, Sequence, List, Tuple
""" import List to precise what is inside of the list """

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
