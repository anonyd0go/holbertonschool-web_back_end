#!/usr/bin/env python3
"""
Retrieve all documents from a MongoDB collection.
"""
from typing import List


def list_all(mongo_collection: object) -> List:
    """
    Finds and returns all documents in a MongoDB collection.

    Args:
        mongo_collection (object): A pymongo collection object.

    Returns:
        List: A list of all documents in the collection.
    """
    docs = list(mongo_collection.find())
    return docs
