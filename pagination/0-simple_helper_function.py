#!/usr/bin/env python3
"""
This module provides a helper function for pagination.

Functions:
    index_range(page: int, page_size: int) -> Tuple[int]:
        Calculates the start and end index for a given page and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int]: Contains start index (inclusive) and end index (exclusive).
    """
    return (page * page_size - page_size, page * page_size)
