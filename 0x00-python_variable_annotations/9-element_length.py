#!/usr/bin/env python3
"""Type-annotated function element_length that takes
    a list input_list of strings and returns a list.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each with a string and its length"""
    return [(i, len(i)) for i in lst]
