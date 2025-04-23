#!/usr/bin/env python3
"""
function to compute the length of elements in an iterable of sequences.

Functions:
    element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
        Returns a list of tuples, each tuple contains a sequence and length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of elements in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        A list of tuples each contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
