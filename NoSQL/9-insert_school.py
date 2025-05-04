#!/usr/bin/env python3
"""
Insert a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: pairs (fields and values) of the document to be inserted.

    Returns:
        The ID of the inserted document.
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
