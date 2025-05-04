#!/usr/bin/env python3
"""
Find schools in a MongoDB collection based on a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns a list of schools that have a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for in the schools' topics.

    Returns:
        list: A list of schools (documents) that match the given topic.
    """
    return list(mongo_collection.find({'topics': topic}))
