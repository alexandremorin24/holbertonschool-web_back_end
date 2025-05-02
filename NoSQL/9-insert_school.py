#!/usr/bin/env python3
""" Function to insert a new document in a collection """
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection using kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
