#!/usr/bin/env python3
"""
This module provides a function that retrieves the first element of a sequence.

Functions:
    safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
        Returns first element of a sequence if it exists, otherwise None.
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Optional[Any]: first element of the sequence if exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
