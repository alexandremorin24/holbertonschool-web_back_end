#!/usr/bin/env python3
""" Function to update topics of a school by name """
def update_topics(mongo_collection, name, topics):
    """Updates the topics of the school document with the given name"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
