#!/usr/bin/env python3
"""
101-safely_get_value.py

This module provides a function to safely retrieve a value from a dictionary.

Functions:
    safely_get_value(dct: MP, key: Any, default: U[T, None] = None) -> U[Any, T]:
        Safely retrieves the value of a key in a dictionary.
"""
from typing import TypeVar, Union, Mapping, Any


T = TypeVar('T')
MP = Mapping
U = Union


def safely_get_value(dct: MP, key: Any, default: U[T, None] = None) -> U[Any, T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (MP): The dictionary to retrieve the value from.
        key (Any): The key to look for in the dictionary.
        default (U[T, None]): The default value to return if the key is not found.

    Returns:
        U[Any, T]: The value associated with the key if it exists.
    """
    if key in dct:
        return dct[key]
    else:
        return default
