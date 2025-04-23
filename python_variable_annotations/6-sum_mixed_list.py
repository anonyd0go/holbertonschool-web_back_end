#!/usr/bin/env python3
"""
Provides a function to compute the sum of a list containing both int and float.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Returns the sum of all elements in a mixed list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing both ints and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of ints and floats.

    Returns:
        float: The sum of all elements in the list as a float.
    """
    return sum(mxd_lst)
