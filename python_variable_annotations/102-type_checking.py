#!/usr/bin/env python3
"""
Provides func "zoom in".

Functions:
    zoom_array(lst: Tuple, factor: int = 2) -> List:
        Returns list where each ele of the tuple is repeated `factor` times.

Variables:
    array (Tuple[int, int, int]): A sample tuple of integers.
    zoom_2x (List): The result of zooming in on `array` with a factor of 2.
    zoom_3x (List): The result of zooming in on `array` with a factor of 3.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on a tuple by repeating its elements a specified number of times.

    Args:
        lst (Tuple): The input tuple to zoom in on.
        factor (int): The num of times to repeat each element. Defaults to 2.

    Returns:
        List: A list where each ele of the tuple is repeated `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
