#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a function that multiplies a float by the multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: the product of the float and the multiplier.
    """

    def multiply(n: float) -> float:
        """
        Multiply a number by the multiplier.

        Args:
            n (float): The number to be multiplied.

        Returns:
            float: The product of `n` and `multiplier`.
        """
        return n * multiplier

    return multiply
