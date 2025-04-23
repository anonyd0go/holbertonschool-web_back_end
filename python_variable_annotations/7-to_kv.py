#!/usr/bin/env python3
"""
function to create a tuple from a string and the square of a number.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Returns a tuple with string and the square of the number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): The number to be squared for the second element.

    Returns:
        Tuple[str, float]: A tuple where with a str and the square of `v`.
    """
    return (k, (v ** 2))
